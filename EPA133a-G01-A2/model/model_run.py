from model import BangladeshModel
from scenarios import ScenarioCreator, ReplicationCreator
# dont forget to import what you need here
from components import Infra
from components import Bridge
from components import Vehicle

"""
    When you run this file it will run the simulation ONLY in the terminal
    The output gets printed out at terminal window below
        This is usefull when wanting to test out instanced classes 
        as well as class functions. 
    To do this:
    place the statements you want to be executed after the model is simulated
    on the bottom of this file, in the order you want them to be executed.
        Most Ideally when you're putting a lot of statements at the bottom no one else is
        going to use you delete them when you're finished when PUSHING to main.
            Or when you want to keep the test and work on them later again, 
            just make a side branch with the name of the thing you were doing like:
            'fixing_datareader_with_test' for example.
                Dont Forget To Import The File and Component/class or function you want to test!
                    When you're finished with a bigger chunk of code use
                    pytest or let pycharm create a file with tests for you.
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
# run_length = 5 * 24 * 60
# seed = 1234567

# run time 1000 ticks oude model
# set to 10 for a fast run
run_length = 10

# Seeds for the different replications
seeds = [0000000, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999]


def run_assignment2():
    scenarios = create_scenarios_assignment2()
    scenario_0 = scenarios[0]
    output = run_scenario_assignment2(scenario_0)
    print("output", output)
    # eigenlijk for loop voor elk scenario, nu maar 1x ivm alleen scenario 0


def create_scenarios_assignment2():
    scenario_factory = ScenarioCreator()
    return scenario_factory.scenarios

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



