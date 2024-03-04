from model import BangladeshModel

class Scenario:
    def __init__(self, a, b, c, d):
        self.category_a_percentage = a
        self.category_b_percentage = b
        self.category_c_percentage = c
        self.category_d_percentage = d

class ScenarioCreator:
    scenarios = []

    def __init__(self, n, create_scenarios_lab_2 = True):
        self.num_scenarios = n
        if (create_scenarios_lab_2):
            self.scenarios = self.create_scenarios_lab_2()

    # Warning: hardcoding - should we perhaps read this in from excel file?
    def create_lab2_scenarios(self):
        s1 = Scenario()
        s2 = Scenario()
        s3 = Scenario()
        s4 = Scenario()
        s5 = Scenario()
        s6 = Scenario()
        s7 = Scenario()
        s8 = Scenario()
        s9 = Scenario()
        s10 = Scenario()
        scenario_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
        return scenario_list


class ModelsCreator:

    # where to place seeds? input or random generator of seeds
    def __init__(self, num_models, runtime, scenario_list = []):
        self.runtime = runtime
        self.N = num_models
        self.scenarios = scenario_list


    def create_models_scenarios(self):
        # error if num_models is unequal to scenario_list length
        seed = 0 # should fix this
        # for all scenarios and numlength create model


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


