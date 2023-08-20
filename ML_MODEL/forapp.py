import pandas as pd
from .data_description import DataDescription
from .null_handler import NullHandler
from .categorical_encoder import CategoricalEncoder
from .feature_scaler import FeatureScaler

def run_preprocessing_cli(filepath, target_column):
    try:
        data = pd.read_csv(filepath)
        independent_data = data.drop(columns=[target_column])

        data_description = DataDescription(independent_data)
        data_description.describe_data()

        null_handler = NullHandler(independent_data)
        print("Null Values in Each Column :")
        null_handler.handle_null()

        categorical_encoder = CategoricalEncoder(independent_data)
        categorical_encoder.encode_categorical()

        feature_scaler = FeatureScaler(independent_data)
        feature_scaler.scale_features()

        return independent_data
    except Exception as e:
        return None
