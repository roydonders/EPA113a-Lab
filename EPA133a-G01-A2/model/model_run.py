from components import Infra
from components import Bridge
from components import Vehicle
from scenarios import ScenarioCreator, ReplicationCreator, Scenario
from dataexporter import DataExporter
import pandas as pd
from pathlib import Path

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
run_length = 300

# Seeds for the different replications
seeds = [1234567, 1111111, 2222222, 3333333, 4444444, 5555555, 6666666, 7777777, 8888888, 9999999]


# this function is defined to orchestrate the simulation process.
# It is called at the end of the script to start the simulation.
def run_assignment2():
    # objects_list = []

    # all scenarios and output for the assignment
    scenarios = create_scenarios_assignment2()
    outputs = run_scenarios_assignment2(scenarios)
    print(f'finished running all the scenarios')

    # # # base scenario_0 variables
    # scenario_0 = scenarios[0]
    # output = run_scenario_assignment2(scenario_0)
    # # print("output", outputs)
    # # eigenlijk for loop voor elk scenario, nu maar 1x ivm alleen scenario 0


def create_scenarios_assignment2():
    print(f'Creating scenarios...')
    scenario_factory = ScenarioCreator()
    print(f'Scenarios created!')
    return scenario_factory.scenarios


def run_scenarios_assignment2(scenarios):
    """
    Runs simulations for each scenario in the list and collects outputs.
    Creates the dataframes that need to be outputted for the assignment
    and then saves the dataframes in CSV inside the "experiment" folder.

    Parameters:
    - scenarios: List of scenario objects

    Returns:
    - list: List of outputs for each scenario.
    """
    outputs = []

    # Initialize DataExporter
    exporter = DataExporter()

    for i, s in enumerate(scenarios):  # Start index from 0
        scenario_name = f'scenario{i}'
        print(f'Scenario {scenario_name} is running now')

        # Run the scenario and receive a tuple with replication as first value and avg__driving time as second
        scenario_output = run_scenario_assignment2(s)
        outputs.append(scenario_output)

        # Extract averege driveing_time from the second value the scenario_output consists of
        avg_driving_time = scenario_output[1]

        # Create dataframe for the scenario
        scenario_results_df = pd.DataFrame({'replication i': range(len(scenario_output[0])),
                                            'avg_driving_time': avg_driving_time})

        # Save scenario dataframe to CSV using DataExporter
        exporter.export_scenario_csv(scenario_results_df, scenario_name)

    return outputs




# Very important to distinguish from run_scenarioS_assignment2!
# This function runs simulations for each SINGLE scenario in the list and collects outputs
def run_scenario_assignment2(scenario):
    # receives a tuple with two values for called method
    output2 = run_replications_assignment2(scenario)
    #output = get_average_driving_times(models)
    return output2 # output is a tuple of 2 values


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



