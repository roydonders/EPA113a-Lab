from model import BangladeshModel
# dont forget to import what you need here
from components import Infra
from components import Bridge
from components import Vehicle
from scenarios import ScenarioCreator, ReplicationCreator, Scenario
import pandas as pd

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
run_length = 1

# Seeds for the different replications
seeds = [0000000, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999]


# this function is defined to orchestrate the simulation process.
# It is called at the end of the script to start the simulation.
def run_assignment2():
    # objects_list = []

    # all scenarios and output for the assignment
    scenarios = create_scenarios_assignment2()
    outputs = run_scenarios_assignment2(scenarios)
    print(f'finished running all the scenarios')

    # # base scenario_0 variables
    # scenario_0 = scenarios[0]
    # output = run_scenario_assignment2(scenario_0)

    # Print output DataFrame for all scenarios
    print_output_dataframe(outputs)

    # Print output in run_terminal
    print("outputs", outputs)
    # eigenlijk for loop voor elk scenario, nu maar 1x ivm alleen scenario 0


def print_output_dataframe(outputs):
    # Create DataFrame
    output_df = pd.DataFrame({'replication i': outputs})
    scenario_name = f'scenario_{Scenario}'
    print(f"Output DataFrame for {Scenario}:")
    print(output_df)

    # Export DataFrame to Excel
    # export_to_excel(output_df)


def export_to_excel(df):
    # Export DataFrame to Excel file
    df.to_excel('data/output_df.xlsx', index=False)
    print("Output DataFrame exported to 'output.xlsx'")



# Creates a list of scenarios using a ScenarioCreator
def create_scenarios_assignment2():
    print(f'Creating scenarios...')
    scenario_factory = ScenarioCreator()
    print(f'Scenarios created!')
    return scenario_factory.scenarios


# Runs simulations for each scenario in the list and collects outputs.
def run_scenarios_assignment2(scenarios):
    outputs = []
    for s in scenarios:
        print(f'scenario {s} is running now')
        o = run_scenario_assignment2(s)
        outputs.append(o)
    return outputs


# Very important to distinguish from run_scenarioS_assignment2!
# This function runs simulations for each SINGLE scenario in the list and collects outputs
def run_scenario_assignment2(scenario):
    models = run_replications_assignment2(scenario)
    output = get_average_driving_times(models)
    return output


# Runs multiple replications for a scenario.
def run_replications_assignment2(scenario):
    replication_factory = ReplicationCreator(run_length, seeds, scenario)
    models = replication_factory.run_replications_assignment2()
    return models


# Computes and returns average driving times from simulation results.
def get_average_driving_times(models):
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


run_assignment2()



# Hieronder oude model
# This is the name of the model that is beinig created
# sim_model = BangladeshModel(seed=seed)

# Check if the seed is set
# print("SEED " + str(sim_model._seed))

# One run with given steps
# for i in range(run_length):
#    sim_model.step()