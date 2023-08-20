import pandas as pd
from data_description import DataDescription
from null_handler import NullHandler
from categorical_encoder import CategoricalEncoder
from feature_scaler import FeatureScaler

class PreprocessingCLI:
    def __init__(self):
        self.data = None
        self.target_variable = None
        self.independent_data = None
    def load_csv(self):
        choice = input(" Do you want to write the name of your dataset file? (y/n): ")
        if choice.lower() == 'y':
            filename = input("Enter the name of the CSV file of dataset (current directory): ")
            filepath = filename
        else:
            filepath = input("Enter the full path to the CSV file: ")

        print("Loading file:", filepath)  # Print for debugging
        print("*************************************************************")
        try:
            self.data = pd.read_csv(filepath)
            print("Dataset loaded successfully.")
        except Exception as e:
            print("Error loading the dataset:", repr(e))

    def choose_target_variable(self):
        target_column = input("Enter the name of the target variable column: ")
        if target_column not in self.data.columns:
            print("Error: Target column not found in the dataset.")
            return
        self.target_variable = target_column
        self.independent_data = self.data.drop(columns=[self.target_variable])
        print(f"Target variable '{target_column}' removed from the dataset.")
        
        print("*************************************************************")

    def preprocess(self):
        if self.independent_data is None:
            print("Error: No dataset loaded or target variable chosen.")
            return
        
        data_description = DataDescription(self.independent_data)
        data_description.describe_data()
        
        print("*************************************************************")
        null_handler = NullHandler(self.independent_data)
        #print("Null Values in Each Column :")
        null_handler.handle_null()
        print("*************************************************************")
        categorical_encoder = CategoricalEncoder(self.independent_data)
        categorical_encoder.encode_categorical()
        print("*************************************************************")
        feature_scaler = FeatureScaler(self.independent_data)
        feature_scaler.scale_features()
        print("*************************************************************")
        print("PREPROCESSING COMPLETED. ENJOY!")
        print("*************************************************************")
    def save_preprocessed_data(self):
        if self.independent_data is None:
            print("Error: No preprocessed data available.")
            return

        output_filename = input("Enter the name for the new preprocessed CSV file: ")
        output_path = f"./{output_filename}"

        try:
            self.independent_data.to_csv(output_path, index=False)
            print(f"Preprocessed data saved as '{output_filename}'.")
        except Exception as e:
            print("Error saving preprocessed data:", e)

if __name__ == "__main__":
    preprocessing_cli = PreprocessingCLI()
    preprocessing_cli.load_csv()
    preprocessing_cli.choose_target_variable()
    preprocessing_cli.preprocess()
    preprocessing_cli.save_preprocessed_data()
