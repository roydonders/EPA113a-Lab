# ---------------------------------------------------------------
import os
import pandas as pd


class DataReader:


    def __init__(self):

        self.path = self.get_path()


    def get_path(self):
        """
        Retrieve the absolute path to a specific CSV file located in a 'data' folder relative to the current script's directory.

        Returns:
            str: The absolute path to the CSV file.

        This method obtains the directory of the current script and then navigates to its parent directory.
        It constructs the path to the 'data' folder within the parent directory and appends the name of the CSV file to it.

        WARNING: Hardcoding
        The method assumes the CSV file is named 'final_n1_network.csv'. If the file name or folder structure changes,
        this method may need to be updated accordingly by differing input variables for the .csv file.
        """
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Get the parent directory
        parent_dir = os.path.dirname(current_dir)

        # Path to the data folder
        data_folder = os.path.join(parent_dir, 'data')

        # Assuming the CSV file is named 'final_n1_network.csv'
        csv_file_path = os.path.join(data_folder, 'final_n1_network.csv')
        return csv_file_path

    def get_roads(self):
        # Read in csv according to predefined path
        csv_import = self.path
        # Read in dataframe
        df_import = pd.read_csv(csv_import)

        return df_import


