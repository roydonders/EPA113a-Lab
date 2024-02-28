# ---------------------------------------------------------------
import os


class DataReader:
    """
    The short expl

    Long explanation

    Class Attributes: TODO below is incorrect
    -----------------
    step_time: int
        step_time = 1 # 1 step is 1 min

    path_ids_dict: defaultdict
        Key: (origin, destination)
        Value: the shortest path (Infra component IDs) from an origin to a destination

        Since there is only one road in the Demo, the paths are added with the road info;
        when there is a more complex network layout, the paths need to be managed differently

    sources: list
        all sources in the network

    sinks: list
        all sinks in the network

    """

    step_time = 1

    def __init__(self):

        self.path = self.get_path()

    """
    bla bla uitleg get_path
    haalt de roads 3 csv op uit data
    """
    def get_path(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Get the parent directory
        parent_dir = os.path.dirname(current_dir)

        # Path to the data folder
        data_folder = os.path.join(parent_dir, 'data')

        # Assuming the CSV file is named '_roads3.csv'
        csv_file_path = os.path.join(data_folder, '_roads3.csv')
        return csv_file_path

    def get_road(self):
        #Previous code for selecting bridges
        # df is inputted dataframe
        # road_specified_df is outputted dataframe
        #road_specified_df = df.loc[df['Road'] == road_specified]
        pass