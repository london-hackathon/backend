import pandas as pd

covid_file = "CardioData.csv"

try:
    # Read the CSV file
    data = pd.read_csv(covid_file)

    # Get column names (attributes)
    attributes = list(data.columns)
    # Print the attributes
    print("Attributes (Column Names) in the CSV File:")
    for attr in attributes:
        print(f"- {attr}")

    
except FileNotFoundError:
    print(f"Error: File not found at {covid_file}. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")