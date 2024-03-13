from model import BangladeshModel
from scenarios import ScenarioCreator

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
run_length = 400

# run time 1000 ticks
# run_length = 1000

# Seeds for the different replications
seeds = [0000000, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999]


# this function is defined to orchestrate the simulation process.
# It is called at the end of the script to start the simulation.
def run_assignment2():
    program = ScenarioCreator(seeds, run_length)
    program.run_scenarios_assignment2()

run_assignment2()
# seed = 1234567
#
# sim_model = BangladeshModel(seed=seed)
#
# # Check if the seed is set
# print("SEED " + str(sim_model._seed))
#
# # One run with given steps
# for i in range(run_length):
#     sim_model.step()
