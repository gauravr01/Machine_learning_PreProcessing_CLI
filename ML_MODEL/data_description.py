class DataDescription:
    def __init__(self, data):
        self.data = data

    def describe_data(self):
        # Get basic summary statistics
        summary = self.data.describe()

        # Print the summary statistics
        print("Data Description:")
        print(summary)
