from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

class CategoricalEncoder:
    def __init__(self, data):
        self.data = data
        self.label_encoder = LabelEncoder()  # Using LabelEncoder
        self.onehot_encoder = OneHotEncoder(sparse_output=False, drop='first')  # Using OneHotEncoder
        
    def encode_categorical(self):
        if self.data.empty:
            print("Error: No data to encode.")
            return
        
        categorical_columns = self.data.select_dtypes(include=['object']).columns
        
        print("Categorical columns:", categorical_columns)
        
        if not categorical_columns.empty:
            for column in categorical_columns:
                encode_choice = input(f"Do you want to encode the '{column}' column? (y/n): ")
                
                if encode_choice.lower() == 'y':
                    encoding_method = input(f"How do you want to encode '{column}'?\n"
                                            "1. Label Encoding\n"
                                            "2. One-Hot Encoding\n"
                                            "Enter your choice (1/2): ")
                    
                    if encoding_method == '1':
                        encoded_values = self.label_encoder.fit_transform(self.data[column])
                        label_mapping = dict(zip(self.label_encoder.classes_, encoded_values))
                        self.data[column] = encoded_values
                        print(f"Label encoding completed for '{column}'.")
                        print("Label mapping:", label_mapping)
                    elif encoding_method == '2':
                        encoded_data = self.onehot_encoder.fit_transform(self.data[[column]])
                        encoded_df = pd.DataFrame(encoded_data, columns=self.onehot_encoder.get_feature_names_out([column]))
                        
                        # Drop the original column and concatenate the encoded columns
                        self.data = pd.concat([self.data.drop(columns=[column]), encoded_df], axis=1)
                        print(f"One-hot encoding completed for '{column}'.")
                    else:
                        print(f"Invalid encoding method choice for '{column}'.")
                else:
                    print(f"'{column}' column not encoded.")
                    todrp = (input(f"Do you want to drop '{column}'.(y/n)"))
                    if todrp.lower() == 'y':
                        self.data.drop(columns=[column], inplace=True)
                        print(f"'{column}' is successfully dropped.")
                    


                
            print("Categorical encoding process completed.")
        else:
            print("No categorical columns found for encoding.")
