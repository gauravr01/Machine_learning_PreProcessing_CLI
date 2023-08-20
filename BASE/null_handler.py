class NullHandler:
    def __init__(self, data):
        self.data = data

    def handle_null(self):
        if self.data.empty:
            print("Error: No data to handle null values.")
            return
        
        # Identify columns with null values
        columns_with_null = self.data.columns[self.data.isnull().any()]
        print("Null Values in Each Column :")
        print(self.data.isnull().sum())

        if not columns_with_null.empty:
            print("Columns with null values:", columns_with_null)
            
            for column in columns_with_null:
                print(f"Handling null values for column '{column}':")
                print("Choose a null handling option:")
                print("1. Fill with mean")
                print("2. Fill with mode")
                print("3. Fill with median")
                print("4. Drop null values")
                print("5. Drop the Column")
                
                choice = input("Enter your choice (1/2/3/4): ")
                
                if choice == '1':
                    fill_value = self.data[column].mean()
                elif choice == '2':
                    fill_value = self.data[column].mode()[0]
                elif choice == '3':
                    fill_value = self.data[column].median()
                elif choice == '4':
                    self.data.dropna(subset=[column], inplace=True)
                    print(f"Null values dropped for column '{column}'.")
                    continue  # Skip filling if dropping
                elif choice == '5':
                    self.data.drop(columns=[column], inplace=True)
                    print(f"Column '{column}' removed.")
                    continue  # Skip filling if removing

                else:
                    print("Invalid choice. Null handling cancelled.")
                    return
                
                self.data[column].fillna(fill_value, inplace=True)
                print(f"Null handling completed for column '{column}'.")
            
            print("All null handling completed.")
        else:
            print("No columns with null values found.")
