from model import BangladeshModel
from scenarios import ScenarioCreator

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
#run_length = 30
run_length = 5 * 24 * 60

# run time 1000 ticks
# run_length = 1000

# Seeds for the different replications
seeds = [0000000, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999]


# All previous code for assignment 2 -> changed into assignment 3 naming for clarity.
# this function is defined to orchestrate the simulation process.
# It is called at the end of the script to start the simulation.
def run_assignment3():
    program = ScenarioCreator(seeds, run_length)
    program.run_scenarios_assignment3()


run_assignment3()


# This function is the old code standard present in the assignment.
# It is not used in the final assignment code, and only present for debugging purposes.
# It only does one run of the model without scenarios/delays.
def one_run():
    seed = 1234567

    sim_model = BangladeshModel(seed=seed)

    # Check if the seed is set
    print("SEED " + str(sim_model._seed))

    # One run with given steps
    for i in range(run_length):
        sim_model.step()


# For debugging
#one_run()
