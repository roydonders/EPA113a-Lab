# This class represents a scenario with probabilities for bridge quality
import pandas as pd

import datareader as dr
from dataexporter import DataExporter
from replications import ReplicationCreator

class Scenario:
    # Class variable to keep track of the next scenario ID
    next_scenario_id = 0

    def __init__(self, a, b, c, d, scenario_id=None):
        # bridge quality categories
        self.category_a_probability = a
        self.category_b_probability = b
        self.category_c_probability = c
        self.category_d_probability = d

        # Automatically assign a unique scenario ID
        self.scenario_id = Scenario.next_scenario_id
        # Increment the next scenario ID for the next scenario
        Scenario.next_scenario_id += 1

    def get_probability(self, s):
        """
        Returns the probability associated with the given category.

        Parameters:
        - s (str): A string representing the category ('A', 'B', 'C', or 'D').

        Returns:
        - float: The probability associated with the given category.

        Raises:
        - ValueError: If the input `s` is not 'A', 'B', 'C', or 'D'.
        """
        if s == 'A':
            return self.category_a_probability
        elif s == 'B':
            return self.category_b_probability
        elif s == 'C':
            return self.category_c_probability
        elif s == 'D':
            return self.category_d_probability
        else:
            raise ValueError("Invalid input. s must be 'A', 'B', 'C', or 'D'.")

    def __str__(self):
        s_id = str(self.scenario_id)
        return f"s{s_id}"


# This class is responsible for creating scenarios
class ScenarioCreator:
    scenarios = []

    # allows for specifying the number of scenarios to create
    def __init__(self, seeds, run_length, n=5, create_scenarios_lab_3=True):
        # number of scenarios
        self.num_scenarios = n
        self.seeds = seeds
        self.run_length = run_length

        if (create_scenarios_lab_3):
            self.create_lab3_scenarios()

    # method creates scenarios for the lab assignment based on predefined probabilities.
    def create_lab2_scenarios(self):
        s0 = Scenario(0,0,0,0)
        s1 = Scenario(0,0,0,0.05)
        s2 = Scenario(0,0,0,0.1)
        s3 = Scenario(0,0,0.05,0.1)
        s4 = Scenario(0,0,0.1,0.2)
        s5 = Scenario(0,0.05,0.1,0.2)
        s6 = Scenario(0,0.1,0.2,0.4)
        s7 = Scenario(0.05,0.1,0.2,0.4)
        s8 = Scenario(0.1,0.2,0.4,0.8)
        #scenario_list = [s0]
        scenario_list = [s0,s1,s2,s3,s4,s5,s6,s7,s8]
        self.scenarios = scenario_list

    # Same for lab 3 - note hardcoding is allowed
    def create_lab3_scenarios(self):
        s0 = Scenario(0,0,0,0)
        s1 = Scenario(0,0,0,0.05)
        s2 = Scenario(0,0,0.05,0.10)
        s3 = Scenario(0,0.05,0.10,0.20)
        s4 = Scenario(0.05,0.10,0.20,0.40)
        scenario_list = [s0,s1,s2,s3,s4]
        self.scenarios = scenario_list

    # Approach if we had to read in from e.g. probabilities from a separate file
    #def create_scenarios_from_excel(self, filename):
        #df = dr.read_df_from_excel(filename)
        # find a way to read the whole dataframe into scenarios and put them in list
        # for each row - create scenario put in list

    def run_scenarios_assignment3(self):
        """
        Runs simulations for each scenario in the list and collects outputs.
        Creates the dataframes that need to be outputted for the assignment
        and then saves the dataframes in CSV inside the "experiment" folder.

        Returns:
        - list: List of outputs for each scenario.
        """
        outputs = []

        # Initialize DataExporter
        exporter = DataExporter()
        scenarios = self.scenarios

        for i, s in enumerate(scenarios):  # Start index from 0
            scenario_name = f'scenario{i}'
            print(f'Scenario {scenario_name} is running now')

            # Run the scenario and receive a tuple with replication as first value and avg__driving time as second
            scenario_output = self.run_scenario_assignment3(s)
            outputs.append(scenario_output)

            # Extract average driveing_time from the second value the scenario_output consists of
            avg_driving_time = scenario_output[1]

            # Create dataframe for the scenario
            scenario_results_df = pd.DataFrame({'replication i': range(len(scenario_output[0])),
                                                'avg_driving_time': avg_driving_time})

            # Save scenario dataframe to CSV using DataExporter
            exporter.export_scenario_csv(scenario_results_df, scenario_name)

        return outputs

    # Very important to distinguish from run_scenarioS_assignment3!
    # This function runs simulations for each SINGLE scenario in the list and collects outputs
    def run_scenario_assignment3(self, scenario):
        # receives a tuple with two values for called method
        output2 = self.run_replications_assignment3(scenario)
        # output = get_average_driving_times(models)
        return output2  # output is a tuple of 2 values

    # Runs multiple replications for a scenario.
    def run_replications_assignment3(self, scenario):
        replication_factory = ReplicationCreator(self.run_length, self.seeds, scenario)
        models = replication_factory.run_replications_assignment3()
        return models





