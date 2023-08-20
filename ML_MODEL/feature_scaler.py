from sklearn.preprocessing import MinMaxScaler

class FeatureScaler:
    def __init__(self, data):
        self.data = data
        self.scaler = MinMaxScaler()  # Using MinMaxScaler for feature scaling

    def scale_features(self):
        if self.data.empty:
            print("Error: No data to scale.")
            return
        
        choice = input("Do you want to scale the numeric features? (y/n): ")
        if choice.lower() == 'y':
            # Identify numeric columns to scale
            numeric_columns = self.data.select_dtypes(include=['float64', 'int64']).columns
            
            if not numeric_columns.empty:
                # Fit the scaler on the data and transform the selected numeric columns
                self.data[numeric_columns] = self.scaler.fit_transform(self.data[numeric_columns])
                print("Feature scaling completed.")
            else:
                print("No numeric columns found for scaling.")
        else:
            print("Numeric features not scaled.")
