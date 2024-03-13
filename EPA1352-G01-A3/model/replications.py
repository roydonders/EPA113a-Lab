# This class is responsible for creating and running replications
# of the model for a given scenario.
from model import BangladeshModel


class ReplicationCreator:

    def __init__(self, runtime, seeds, scenario, n=10):
        self.runtime = runtime
        # Need to check if N = length seeds!!!
        # N is number of replications for ReplicationCreator class
        self.N = n
        self.seeds = seeds
        self.scenario = scenario

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
        return [100]
        average_drive_times = []

        for model in final_models:
            driving_times = model.schedule.drivingtimes
            total_drive_time = sum(driving_times)
            total_vehicles = len(driving_times)  # Count vehicles that have a driving_time
            average_drive_time = total_drive_time / total_vehicles if total_vehicles != 0 else 0
            average_drive_times.append(average_drive_time)

        return average_drive_times

    # method executes the model for each replication and collects the results
    def create_replications(self, scenario):
        replications = []
        n = self.N

        for i in range(n):
            seed = self.seeds[i]
            print("Creating Replication", i, "with seed", seed)
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
