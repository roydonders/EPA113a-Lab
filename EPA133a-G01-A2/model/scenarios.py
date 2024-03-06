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

    # where to place seeds? input or random generator of seeds
    # meegeven dat hij ook een aantal replications kan doen?
    def __init__(self, runtime, seeds, scenario_name, n = 10):
        self.runtime = runtime
        # Need to check if N = length seeds!!!
        # N is number of replications for ReplicationCreator class
        self.N = n
        self.seeds = seeds
        self.scenario_name = scenario_name
        # print(self.scenario_name)


    # hier moet dan nog een export methode komen
    # method runs replications for the specified scenario.
    def run_replications_assignment2(self):
        for i in range(self.N):
            replications = self.create_replications()
            final_models = self.run_replications(replications)
            total_driving_time = sum([vehicle.driving_time for model in final_models for vehicle in
                                      model.schedule.agents if isinstance(vehicle, Vehicle)])
            total_vehicles = sum([1 for model in final_models for vehicle in model.schedule.agents
                                  if isinstance(vehicle, Vehicle)])
            total_average_driving_time = total_driving_time / total_vehicles if total_vehicles != 0 else 0
            print("After", self.N, "Replications: Average Driving Time:", total_average_driving_time)

    # method executes the model for each replication and collects the results
    def create_replications(self):
        replications = []
        n = self.N

        for i in range(n):
            seed = self.seeds[i]
            print("Creating Replication", i,"with seed", seed)
            model_i = self.create_single_model(seed, self.scenario_name, i)

            replications.append(model_i)
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

    # creates a single model instance(BangladeshModel) for a replication.
    # It initializes the model with the provided seed, scenario, and replication number.
    def create_single_model(self, seed, scenario_name, rep_number):
        # Ensure scenario_name is a string
        scenario_name_str = str(scenario_name)
        sim_model = BangladeshModel(seed=seed, scenario_name=scenario_name_str, replication = rep_number)
        sim_model.replication_number = rep_number
        sim_model.scenario_name = scenario_name_str
        # here a scenario should be passed to
        # Check if the seed is set
        print("SEED " + str(sim_model._seed))
        return sim_model

    def run_single_model(self, sim_model):
        run_length = self.runtime
        for i in range(run_length):
            sim_model.step()
        return sim_model


# EOF -----------------------------------------------------------