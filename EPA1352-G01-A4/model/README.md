# Simple Transport Model Demo in MESA

Created by:
Yilin HUANG

Email:
y.huang@tudelft.nl

Version:
1.3

Expanded upon by:
Group 01

Email:
T.Otter@student.tudelft.nl

## Introduction

A simple transport model demo in MESA for EPA133a Advanced Simulation course Assignment 3.
Expanded upon to experiment with N1, N2 and sideroads data.

## How to Use

- Create and activate a virtual environment

In PyCharm, you can create a virtual environment by following the steps below:

    1. Open the project in PyCharm
    2. Go to Settings -> Project: epa133a -> Python Interpreter
    3. Click "Add Interpreter"
    4. Select "Add Local Interpreter"
    5. Select Virtualenv Environment
    6. Select New environment
    7. Select Base interpreter as Python 3.11
    8. Click OK and also close the settings with OK

Afterwards, you should see "Python 3.11" (epa133a) in the bottom-right corner of the PyCharm window.
To install the requirements, open a terminal/command line window in PyCharm and type:

```
    $ pip install -r requirements.txt
```

- Launch the simulation model with visualization

```
    $ python model_viz.py
```

- Launch the simulation model without visualization

```
    $ python model_run.py
```

## Original Files

- [model.py](model.py): Contains the model `BangladeshModel` which is a subclass of Mesa `Model`. It reads a `csv` file with specific format for (transport) model generation. (See the README in the `data` directory for data format.) In addition to dynamic behavior, each model component instance (i.e., object) also has geo-location variables, i.e. latitude and longitude in Decimal Degrees (DD). The given bounds of the latitude and longitude of all objects are translated into the bounds of the HTML5 canvas, which is used in case the visualization is launched.

  In this file, the BangladeshModel is modified according to the assignment.

- [components.py](components.py): Contains the model component definitions for the (main) model. Check the file carefully to see which components are already defined.

  In this file, you modify and add your own components. Note that the Bridge and Vehicle component is expanded upon.

- [model_viz.py](model_viz.py): Sets up the visualization; uses the `SimpleCanvas` element defined. Calls the model. Run the visualization server.

  In this file, simple visualization is defined.

- [model_run.py](model_run.py): Sets up the model run (conditions). Calls the model. Run the simulation without visualization.

  In this file, model batch runs are defined.

- [ContinuousSpace](ContinuousSpace): The directory contains files needed to visualize Python3 Mesa models on a continuous canvas with geo-coordinates, a functionality not contained in the current Mesa package.

- [ContinuousSpace/SimpleContinuousModule.py](ContinuousSpace/SimpleContinuousModule.py): Defines `SimpleCanvas`, the Python side of a custom visualization module for drawing objects with continuous positions. This is a slight adaptation of the Flocker example provided by the Mesa project.

- [ContinuousSpace/simple_continuous_canvas.js](ContinuousSpace/simple_continuous_canvas.js): JavaScript side of the `SimpleCanvas` visualization module. It takes the output generated by the Python `SimpleCanvas` element and draws it in the browser window via HTML5 canvas. It can draw circles and rectangles. Both can have text annotation. This file is an adaptation of the Flocker example provided by the Mesa project.

## Added Files and Classes

- [scenarios.py](scenarios.py): This file contains classes for defining scenarios of a model.

  - `Scenario`: Represents a scenario with probabilities for bridge quality. It defines the probabilities for different categories ('A', 'B', 'C', 'D') and provides a method to retrieve the probability associated with a specific category.

  - `ScenarioCreator`: Responsible for creating scenarios. It offers the ability to create scenarios for a lab assignment based on predefined probabilities.

  Example usage:

  ```python
  # Example usage:
  scenario_creator = ScenarioCreator()
  scenario = scenario_creator.scenarios[0]  # Select a scenario from the list of created scenarios
  replication_creator = ReplicationCreator(runtime=100, seeds=[123, 456, 789], scenario=scenario, n=3)
  final_models, average_drive_time = replication_creator.run_replications_assignment3()

  # Access results
  for model in final_models:
      for driving_time in model.schedule.drivingtimes:
          print(driving_time)  # Print driving time for all vehicles in terminal
  print("Average Drive Time:", average_drive_time)  # Print average drive time

- [replications.py](replications.py): This file is responsible for creating and running replications of the model for a given scenario.

  - `ReplicationCreator`: Responsible for creating and running replications/models. It offers the ability to create replications for a lab assignment.

- [datareader.py](datareader.py): This file contains a class for reading data from a specified CSV file. It assumes the CSV file is named 'final_n1_network.csv' (please see the jupyter notebook)

  - `DataReader`: A class for reading data from a CSV file. It includes methods for obtaining the absolute path to the CSV file and for retrieving the data from the file.

- [dataexporter.py](dataexporter.py): This file contains a class for exporting data to CSV files.

  - `DataExporter`: A class for exporting data to CSV files. It includes methods for initializing the object and exporting scenario DataFrame to a CSV file.

    Constructor Parameters:
    - `folder_name` (str): Name of the folder where CSV files will be saved. Default is "experiment".

