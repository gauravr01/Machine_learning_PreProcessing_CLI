import pandas as pd
from data_description import DataDescription
from null_handler import NullHandler
from categorical_encoder import CategoricalEncoder
from feature_scaler import FeatureScaler

# #def run_preprocessing_cli(filepath, target_column):
#     try:
#         data = pd.read_csv(filepath)
#         independent_data = data.drop(columns=[target_column])

#         data_description = DataDescription(independent_data)
#         data_description.describe_data()

#         #columns = data.columns.tolist()
#         #print(columns)

#         null_handler = NullHandler(independent_data)
#         print("Null Values in Each Column :")
#         null_handler.handle_null()

#         categorical_encoder = CategoricalEncoder(independent_data)
#         categorical_encoder.encode_categorical()

#         feature_scaler = FeatureScaler(independent_data)
#         feature_scaler.scale_features()

#         return independent_data 
#     except Exception as e:
#         return None
def run_preprocessing_cli(filepath, target_column, preprocessing_steps):
    try:
        data = pd.read_csv(filepath)
        independent_data = data.drop(columns=[target_column])

        data_description = DataDescription(independent_data)
        data_description.describe_data()

        if 'null_handling' in preprocessing_steps:
            null_handler = NullHandler(independent_data)
            print("Null Values in Each Column :")
            null_handler.handle_null()

        if 'categorical_encoding' in preprocessing_steps:
            categorical_encoder = CategoricalEncoder(independent_data)
            categorical_encoder.encode_categorical()

        if 'feature_scaling' in preprocessing_steps:
            feature_scaler = FeatureScaler(independent_data)
            feature_scaler.scale_features()
    
        preprocessed_data_dict = independent_data.to_dict(orient='records')

        return preprocessed_data_dict
    except Exception as e:
        return None
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