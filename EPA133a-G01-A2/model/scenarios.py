from model import BangladeshModel
class Scenario:
    def __init__(self, a, b, c, d):
        self.category_a_probability = a
        self.category_b_probability = b
        self.category_c_probability = c
        self.category_d_probability = d
        # hier replications toevoegen?

class ScenarioCreator:
    scenarios = []

    def __init__(self, n, create_scenarios_lab_2 = True):
        self.num_scenarios = n
        if (create_scenarios_lab_2):
            self.scenarios = self.create_lab2_scenarios()

    # Warning: hardcoding - should we perhaps read this in from excel file?
    def create_lab2_scenarios(self):
        s0 = Scenario(0,0,0,0)
        # s1 = Scenario(0,0,0,0.05)
        # s2 = Scenario(0,0,0,0.1)
        # s3 = Scenario(0,0,0.05,0.1)
        # s4 = Scenario(0,0,0.1,0.2)
        # s5 = Scenario(0,0.05,0.1,0.2)
        # s6 = Scenario(0,0.1,0.2,0.4)
        # s7 = Scenario(0.05,0.1,0.2,0.4)
        # s8 = Scenario(0.1,0.2,0.4,0.8)
        scenario_list = [s0]
        # scenario_list = [s0,s1,s2,s3,s4,s5,s6,s7,s8]
        return scenario_list


class ModelsCreator:

    # where to place seeds? input or random generator of seeds
    # meegeven dat hij ook een aantal replications kan doen?
    def __init__(self, runtime, seeds, scenario, n = 10):
        self.runtime = runtime
        # Need to check if N = length seeds!!!
        self.N = n
        self.seeds = seeds
        self.scenario = scenario
    # hier moet dan nog een export methode komen
    def run_replications_assignment2(self):
        reps = self.create_replications()
        finalmodels = self.run_replications(reps)
        return finalmodels

    def create_replications(self):
        replications = []
        n = self.N
        for i in range(n):
            seed = self.seeds[i]

            modeli = self.create_single_model(seed)

            replications.append(modeli)
        return replications

    def run_replications(self, replications):
        finalmodels = []
        for rep in replications:
            rep = self.run_single_model(rep)
            finalmodels.append(rep)
        return finalmodels

    def create_single_model(self, seed):
        sim_model = BangladeshModel(seed=seed)
        # here a scenario should be passed to
        # Check if the seed is set
        print("SEED " + str(sim_model._seed))
        return sim_model

    def run_single_model(self, sim_model):
        run_length = self.runtime
        for i in range(run_length):
            sim_model.step()
        return sim_model


