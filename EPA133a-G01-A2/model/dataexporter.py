import pandas as pd

class DataExporter:
    def write_csv_file(self, filename, df):
        """
        Write DataFrame to a CSV file with given filename.

        Args:
            filename (str): The name of the CSV file to write.
            df (DataFrame): Pandas DataFrame to be written to the CSV file.
        """
        df.to_csv(filename, index=False)

    def convert_driving_times_to_csv(self, dataframes):
        """
        Convert list of Pandas DataFrames of average driving times into CSV files with appropriate titles.

        Args:
            dataframes (list): A list of Pandas DataFrames containing average driving times to be converted.
        """
        for i, df in enumerate(dataframes):
            # Generate filename for the CSV file
            filename = f"scenario{i}.csv"

            # Write data to the CSV file
            self.write_csv_file(filename, df)

# Example usage:
exporter = DataExporter()

# Sample dataframes (you can replace this with your actual dataframes)
df1 = pd.DataFrame({'Day': [1, 2, 3, 4], 'Average Driving Time': [1.5, 2.0, 1.8, 1.6]})
df2 = pd.DataFrame({'Day': [1, 2, 3, 4], 'Average Driving Time': [2.2, 1.9, 2.5, 2.3]})
df3 = pd.DataFrame({'Day': [1, 2, 3, 4], 'Average Driving Time': [1.7, 1.8, 1.6, 1.9]})
dataframes = [df1, df2, df3]

# Convert list of dataframes to CSV files
exporter.convert_driving_times_to_csv(dataframes)
