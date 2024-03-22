import networkx as nx
from matplotlib import pyplot as plt
from mesa import Model
from mesa.time import BaseScheduler
from mesa.space import ContinuousSpace
from components import Source, Sink, SourceSink, Bridge, Link, Intersection
from datareader import DataReader
import pandas as pd
from collections import defaultdict


# ---------------------------------------------------------------
def set_lat_lon_bound(lat_min, lat_max, lon_min, lon_max, edge_ratio=0.02):
    """
    Set the HTML continuous space canvas bounding box (for visualization)
    give the min and max latitudes and Longitudes in Decimal Degrees (DD)

    Add white borders at edges (default 2%) of the bounding box
    """

    lat_edge = (lat_max - lat_min) * edge_ratio
    lon_edge = (lon_max - lon_min) * edge_ratio

    x_max = lon_max + lon_edge
    y_max = lat_min - lat_edge
    x_min = lon_min - lon_edge
    y_min = lat_max + lat_edge
    return y_min, y_max, x_min, x_max


# ---------------------------------------------------------------

class BangladeshModel(Model):
    """
    The main (top-level) simulation model

    One tick represents one minute; this can be changed
    but the distance calculation need to be adapted accordingly

    Class Attributes:
    -----------------
    step_time: int
        step_time = 1 # 1 step is 1 min

    path_ids_dict: defaultdict
        Key: (origin, destination)
        Value: the shortest path (Infra component IDs) from an origin to a destination

        Only straight paths in the Demo are added into the dict;
        when there is a more complex network layout, the paths need to be managed differently
        The above is done with the Assignment 3 changes below.

    sources: list
        all sources in the network

    sinks: list
        all sinks in the network

    """

    step_time = 1

    # Not used anymore due to separate datareader class
    # file_name = '../data/demo-4.csv'

    def __init__(self, seed=None, x_max=500, y_max=500, x_min=0, y_min=0, scenario=None):

        self.G = None
        self.roads = None
        self.schedule = BaseScheduler(self)
        self.schedule.drivingtimes = []
        self.running = True
        # Paths id changed to standard dictionary
        self.path_ids_dict = {}
        self.space = None
        self.sources = []
        self.sinks = []
        self.seed = seed
        self.scenario = scenario

        self.generate_model()
        print("Generated model")

    def generate_model(self):
        """
        generate the simulation model according to the csv file component information

        Warning: the labels are the same as the csv column labels
        """

        # Not used anymore - kept for clarity
        # df = pd.read_csv(self.file_name)

        # Read in data
        df = read_in_data()

        # a list of names of roads to be generated
        # Changed: Read the road list in automatically
        roads = df['road'].unique().tolist()
        # Print for debugging/clarification
        print(roads)
        self.roads = roads

        df_objects_all = []
        for road in roads:
            # Select all the objects on a particular road in the original order as in the cvs
            df_objects_on_road = df[df['road'] == road]

            if not df_objects_on_road.empty:
                df_objects_all.append(df_objects_on_road)

                """
                NO LONGER USED, KEPT IN CODE/COMMENT FOR CLARIFICATION (what is changed in the code)
                Set the path 
                1. get the serie of object IDs on a given road in the cvs in the original order
                2. add the (straight) path to the path_ids_dict
                3. put the path in reversed order and reindex
                4. add the path to the path_ids_dict so that the vehicles can drive backwards too
                """
                # path_ids = df_objects_on_road['id']
                # path_ids.reset_index(inplace=True, drop=True)
                # self.path_ids_dict[path_ids[0], path_ids.iloc[-1]] = path_ids
                # self.path_ids_dict[path_ids[0], None] = path_ids
                # path_ids = path_ids[::-1]
                # path_ids.reset_index(inplace=True, drop=True)
                # self.path_ids_dict[path_ids[0], path_ids.iloc[-1]] = path_ids
                # self.path_ids_dict[path_ids[0], None] = path_ids

        # put back to df with selected roads so that min and max and be easily calculated
        df = pd.concat(df_objects_all)

        # Changed: Generate nx model, call the graph G and store it as class variable
        self.G = generate_nx_model(df)
        print("Generated NX model")
        y_min, y_max, x_min, x_max = set_lat_lon_bound(
            df['lat'].min(),
            df['lat'].max(),
            df['lon'].min(),
            df['lon'].max(),
            0.05
        )

        # ContinuousSpace from the Mesa package;
        # not to be confused with the SimpleContinuousModule visualization
        self.space = ContinuousSpace(x_max, y_max, True, x_min, y_min)

        for df in df_objects_all:
            for _, row in df.iterrows():  # index, row in ...

                # create agents according to model_type
                model_type = row['model_type'].strip()
                agent = None

                name = row['name']
                if pd.isna(name):
                    name = ""
                else:
                    name = name.strip()

                if model_type == 'source':
                    agent = Source(row['id'], self, row['length'], name, row['road'])
                    self.sources.append(agent.unique_id)
                elif model_type == 'sink':
                    agent = Sink(row['id'], self, row['length'], name, row['road'])
                    self.sinks.append(agent.unique_id)
                elif model_type == 'sourcesink':
                    agent = SourceSink(row['id'], self, row['length'], name, row['road'])
                    self.sources.append(agent.unique_id)
                    self.sinks.append(agent.unique_id)
                elif model_type == 'bridge':
                    # Added: Each bridge now stores if it is broken
                    cond = row['condition']
                    broken = self.determine_if_bridge_broken(cond)
                    agent = Bridge(row['id'], self, row['length'], row['name'], row['road'], cond, broken=broken,
                                   seed=self._seed)
                elif model_type == 'link':
                    agent = Link(row['id'], self, row['length'], name, row['road'])
                elif model_type == 'intersection':
                    if not row['id'] in self.schedule._agents:
                        agent = Intersection(row['id'], self, row['length'], name, row['road'])

                if agent:
                    self.schedule.add(agent)
                    y = row['lat']
                    x = row['lon']
                    self.space.place_agent(agent, (x, y))
                    agent.pos = (x, y)

    def get_random_route(self, source):
        """
        pick up a random route given an origin
        """
        while True:
            # different source and sink
            sink = self.random.choice(self.sinks)
            if sink is not source:
                break
        # Debugging prints
        print(f"I come from {source} and will go to {sink}")
        path = self.lookup_path(source, sink)
        print(f"And thus I will travel path {path}")
        return path

    def get_route(self, source):
        # Changed to return random route instead of straight route
        return self.get_random_route(source)

    # Added methods lookup path and calculate the shortest path
    def lookup_path(self, source, sink):
        """
        Lookup the shortest path between two nodes.

        Args:
            source: Source node.
            sink: Sink node.

        Returns:
            list: List representing the shortest path between source and sink.
        """
        # Try to return the (shortest) path from paths dictionary, but calculate/store first if not yet present
        if (source, sink) not in self.path_ids_dict:
            self.calculate_shortest_path(source, sink)

        return self.path_ids_dict[source, sink]

    def calculate_shortest_path(self, source, sink):
        """
        Calculate the shortest path between two nodes using NetworkX & Dijkstra's Algorithm.

        Args:
            source: Source node.
            sink: Sink node.
        """
        # Calculate the shortest path using Dijkstra's Algorithm and class variable G
        path = nx.dijkstra_path(self.G, source, sink)
        # store in path dictionary
        self.path_ids_dict[source, sink] = path

    def get_straight_route(self, source):
        """
        pick up a straight route given an origin
        """
        return self.path_ids_dict[source, None]

    def step(self):
        """
        Advance the simulation by one step.
        """
        self.schedule.step()

    def determine_if_bridge_broken(self, cond):
        if self.scenario is None:
            return False

        # Check if seed is set
        seed = self.seed
        if seed is None:
            raise ValueError("Seed must be provided for reproducibility.")
        # Get the probability of breaking from the datafile: p
        p = self.scenario.get_probability(cond)
        # Derive a random test_pE(0,1) from self.random
        test_p = self.random.random()
        # Determine if the bridge is broken or not
        broken = test_p < p
        return broken


# Below are newly added methods for assignment 3
def read_in_data():
    """
    Read road data using DataReader.

    Returns:
        pandas.DataFrame: DataFrame containing road data.
    """
    dr = DataReader()
    df = dr.get_roads()
    return df


def generate_nx_model(df):
    """
    Generate a NetworkX graph model from a DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing road network data.

    Returns:
        nx.Graph: NetworkX graph representing the road network.
    """
    # Convert lat and lon columns to numeric
    # df['lat'] = pd.to_numeric(df['lat'])
    # df['lon'] = pd.to_numeric(df['lon'])

    # Create a graph
    G = nx.Graph()

    # Add nodes and edges with weights from the dataframe
    G = add_nodes(G, df)
    G = add_edges(G, df)

    # Optional: plot the network for debugging purposes
    plot_network(G)
    return G


def add_nodes(G, df):
    """
    Add nodes to the graph.

    Args:
        G (nx.Graph): NetworkX graph.
        df (pandas.DataFrame): DataFrame containing road network data.

    Returns:
        nx.Graph: NetworkX graph with added nodes.
    """
    # Add nodes
    for index, row in df.iterrows():
        longitude = row['lon']
        latitude = row['lat']

        # Give a node corresponding id, longitude, and latitude
        G.add_node(row['id'], pos=(longitude, latitude))
    return G


def add_edges(G, df):
    """
    Add edges to the graph based on the road.

    Args:
        G (nx.Graph): NetworkX graph.
        df (pandas.DataFrame): DataFrame containing road network data.

    Returns:
        nx.Graph: NetworkX graph with added edges.
    """
    # Add edges based on the road
    for road in df['road'].unique():
        # Add edges for each road separately, by making a copy of the df per road
        road_df = df[df['road'] == road]

        # For each node (not at the end), add an edge
        for i in range(len(road_df) - 1):
            # current node
            u = road_df.iloc[i]['id']
            # next node
            v = road_df.iloc[i + 1]['id']
            # weight
            w = road_df.iloc[i]['length']

            # Add edge
            G.add_edge(u, v, weight=w)
    return G


def plot_network(G):
    """
    Plot the network graph. Optional, helpful for debugging.

    Args:
        G (nx.Graph): NetworkX graph to be plotted.
    """
    # Optional method for plotting/debugging
    # Test for calculating shortest path (optional)
    # path = nx.dijkstra_path(G, 1000000, 1000013)
    # print(f"shortest path is {path}")
    # Plotting
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(60, 38))
    # Draw nodes
    nx.draw(G, pos, with_labels=True, node_size=50, node_color='orange', font_size=5)
    labels = nx.get_edge_attributes(G, 'weight')
    # Draw edges
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='darkred', font_size=7)
    # Titles and Grid
    plt.title('Road Network')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()

# EOF -----------------------------------------------------------
