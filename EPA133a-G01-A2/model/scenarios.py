# # remove model from import because of circular dependencie
from model import BangladeshModel
from components import Vehicle


# This class represents a scenario with probabilities for bridge quality
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
    def __init__(self, n = 9, create_scenarios_lab_2 = True):
        # number of scenarios
        self.num_scenarios = n

        if (create_scenarios_lab_2):
            self.scenarios = self.create_lab2_scenarios()

    # method creates scenarios for the lab assignment based on predefined probabilities.
    # Warning: hardcoding - should we perhaps read this in from excel file?
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
        return scenario_list


# This class is responsible for creating and running replications
# of the model for a given scenario.
class ReplicationCreator:

    def __init__(self, runtime, seeds, scenario, n = 10):
        self.runtime = runtime
        # Need to check if N = length seeds!!!
        # N is number of replications for ReplicationCreator class
        self.N = n
        self.seeds = seeds
        self.scenario = scenario


    # hier moet dan nog een export methode komen
    # method runs replications for the specified scenario.
    def run_replications_assignment2(self):

        # creates replications for teh scenario passed
        replications = self.create_replications(self.scenario)  # Pass scenario and seeds here
        # all replications for all scenarios are stored in final models
        final_models = self.run_replications(replications)

        # calculate the average driving time for all vehicles
        average_drive_time = self.calculate_average_drive_time(final_models)

        # # Print list of driving times of all vehicles
        # print("List of Driving Times of All Vehicles:")
        # for model in final_models:
        #     for driving_time in model.schedule.drivingtimes:
        #         # print driving time for all vehicles in terminal
        #         print(driving_time)
        # # Print average drive time
        print("Average Drive Time:", average_drive_time)

        return final_models, average_drive_time

    def calculate_average_drive_time(self, final_models):
        # Flatten the list of driving times
        total_drive_times = [driving_time for model in final_models for driving_time in model.schedule.drivingtimes]

        if total_drive_times:
            total_vehicles = len(total_drive_times)
            print(total_vehicles)
            total_drive_time = sum(total_drive_times)
            print(total_drive_time)
            average_drive_time = total_drive_time / total_vehicles
            print(average_drive_time)
        else:
            average_drive_time = 0  # Handle the case when no vehicles arrived at sinks
        return average_drive_time


    # method executes the model for each replication and collects the results
    def create_replications(self, scenario):
        replications = []
        n = self.N

        for i in range(n):

            seed = self.seeds[i]
            print("Creating Replication", i,"with seed", seed)
            modeli = self.create_single_model(seed, scenario)

            replications.append(modeli)
        return replications

    # method executes the model for each replication and collects the results
    def run_replications(self, replications):
        finalmodels = []
        n = self.N
        for i in range(n):
            rep = replications[i]
            print("Running Replication", i)
            rep = self.run_single_model(rep)
            finalmodels.append(rep)
        return finalmodels

    def create_single_model(self, seed, scenario):
        sim_model = BangladeshModel(seed=seed, scenario=scenario)
        # here a scenario should be passed to
        # Check if the seed is set
        print("SEED " + str(sim_model._seed))
        return sim_model

    def run_single_model(self, sim_model):
        run_length = self.runtime
        for i in range(run_length):
            sim_model.step()
        return sim_model


