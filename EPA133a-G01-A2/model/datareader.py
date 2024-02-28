# ---------------------------------------------------------------
import os
import pandas as pd


class DataReader:
    """
    The short expl

    Long explanation

    Class Attributes: TODO below is incorrect
    -----------------
    step_time: int
        step_time = 1 # 1 step is 1 min

    path_ids_dict: defaultdict
        Key: (origin, destination)
        Value: the shortest path (Infra component IDs) from an origin to a destination

        Since there is only one road in the Demo, the paths are added with the road info;
        when there is a more complex network layout, the paths need to be managed differently

    sources: list
        all sources in the network

    sinks: list
        all sinks in the network

    """

    step_time = 1

    def __init__(self):

        self.path = self.get_path()

        self.get_roads()

    def get_path(self):
        """
        Retrieve the absolute path to a specific CSV file located in a 'data' folder relative to the current script's directory.

        Returns:
            str: The absolute path to the CSV file.

        This method obtains the directory of the current script and then navigates to its parent directory.
        It constructs the path to the 'data' folder within the parent directory and appends the name of the CSV file to it.

        WARNING: Hardcoding
        The method assumes the CSV file is named '_roads3.csv'. If the file name or folder structure changes,
        this method may need to be updated accordingly by differing input variables for the .csv file.
        """
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Get the parent directory
        parent_dir = os.path.dirname(current_dir)

        # Path to the data folder
        data_folder = os.path.join(parent_dir, 'data')

        # Assuming the CSV file is named '_roads3.csv'
        csv_file_path = os.path.join(data_folder, '_roads3.csv')
        return csv_file_path

    def get_roads(self):
        csv_import = self.get_path()
        df_import = pd.read_csv(csv_import)
        df_import = df_import.drop(columns=['name', 'lrp'])

        return print(df_import.head(10))