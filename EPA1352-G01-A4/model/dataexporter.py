import pandas as pd
from pathlib import Path

class DataExporter:
    def __init__(self, folder_name="experiment"):
        """
        Initializes the DataExporter object.

        Parameters:
        - folder_name (str): Name of the folder where CSV files will be saved.
        """
        # Find parent directory of the current Python script
        parent_dir = Path(__file__).resolve().parent.parent
        self.output_folder = parent_dir / folder_name
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def export_scenario_csv(self, scenario_df, scenario_name):
        """
        Exports scenario DataFrame to a CSV file.

        Parameters:
        - scenario_df (DataFrame): DataFrame containing scenario data.
        - scenario_name (str): Name of the scenario for file naming.
        """
        output_filename = f'{scenario_name}.csv'
        output_path = self.output_folder / output_filename
        scenario_df.to_csv(output_path, index=False)
        print(f"Output DataFrame for Scenario {scenario_name} saved to {output_path}")


