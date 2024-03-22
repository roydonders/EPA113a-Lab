# README File

Created by: EPA133a Group 01

|         Name          | Student Number |
| :-------------------: | :------------: |
| Fred Nieuwenhuijzen  |     4353943    |
| Timon Otter           |     5884586    |
| Bram Verbeek          |     4962850    |
| Lukas van der Wolf    |     5150264    |

## Introduction

Thank you for using our model and program.

This assignment focuses on model generation and component building using Mesa, a Python3 agent-based simulation environment. Please note that this assignment builds upon previous work (the Demo model kindly provided to us & Assignment 2).

Our objective is to study the effects of bridge maintenance or unavailability on average travel times for a major road in Bangladesh.

Mesa's object-oriented approach simplifies the creation of user-defined models and libraries, allowing us to develop a demo model of goods transport over selected roads in Bangladesh. Bridges and ferries are crucial components of Bangladesh's transport system, often causing delays after natural disasters.

We aim to automatically generate a Mesa model to analyze the impact of bridge conditions on traffic along the N1 and N2 roads and several side roads (for more information, please see the detailed description of this in the attached report). Trucks' movement from ends of the roads will be simulated, measuring delays and travel times.

The assignment entails creating a "business as usual" model (Scenario 0) and introducing scenarios with varying probabilities of bridge breakdowns for different quality categories (A to D). Each scenario will be replicated 10 times to assess reliability.

Output files, named "scenario1.csv", "scenario2.csv", etc., will be placed in the "experiment" folder of the submission directory "EPA133a-G01-A2". We'll analyze the effects of each scenario on truck driving time and discuss the results in a report.

If you are looking for information about the Demo model of Assignment 3, navigate to the [model/README.md](model/README.md) in the [model](model) directory.

## How to Use

To access the experiment results, navigate to the "experiment" folder. Here, you'll find CSV files containing the output data for each scenario.

If you wish to run the model and generate the experiment results yourself:

1. Navigate to the "models" directory.

2. Run the `model_run.py` file using Python 3.11 or 3.12

This will execute the model with predefined seeds used in our experiments.

3. The experiment results will be generated as CSV files using the specified seeds. Feel free to modify parameters such as seeds or runtime in the `model_run.py` file for your own experimentation.

### Main files

The model_run.py creates 5 predefined scenarios and 10 replications per scenario using scenarios.py/replications.py (please see attached the report for additional information).

datareader.py is used for reading data in, dataexporter.py is used for exporting data.

For more details, please see the README in the models folder.

