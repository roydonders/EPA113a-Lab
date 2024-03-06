from model import BangladeshModel
# dont forget to import what you need here
from components import Infra
from components import Bridge
from components import Vehicle
from scenarios import ScenarioCreator, ReplicationCreator

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
# run_length = 5 * 24 * 60
# seed = 1234567

# run time 1000 ticks oude model
# run_length = 1000
# set to 10 for a fast run
run_length = 1000

# Seeds for the different replications
seeds = [0000000, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999]



def run_assignment2():
    scenarios = create_scenarios_assignment2()
    outputs = run_scenarios_assignment2(scenarios)
    scenario_0 = scenarios[0]
    output = run_scenario_assignment2(scenario_0)
    print("output", outputs)
    # eigenlijk for loop voor elk scenario, nu maar 1x ivm alleen scenario 0


def create_scenarios_assignment2():
    scenario_factory = ScenarioCreator()
    return scenario_factory.scenarios

def run_scenarios_assignment2(scenarios):
    outputs = []
    for s in scenarios:
        o = run_scenario_assignment2(s)
        outputs.append(o)
    return outputs

def run_scenario_assignment2(scenario):
    models = run_replications_assignment2(scenario)
    output = get_average_driving_times(models)
    return output

def run_replications_assignment2(scenario):
    replication_factory = ReplicationCreator(run_length, seeds, scenario)
    models = replication_factory.run_replications_assignment2()
    return models

def get_average_driving_times(models):
    return [0,0,0,0,0,0,0,0,0,0]


run_assignment2()

# Hieronder oude model
# This is the name of the model that is beinig created
# sim_model = BangladeshModel(seed=seed)

# Check if the seed is set
# print("SEED " + str(sim_model._seed))

# One run with given steps
# for i in range(run_length):
#    sim_model.step()



