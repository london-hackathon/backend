import pandas as pd

def raceEthnicityCount(covid_file, race_col="Race"):
    try:
        # Read the CSV file
        data = pd.read_csv(covid_file)

        # Get column names (attributes)
        attributes = list(data.columns)
        # Print the attributes
        #print("Attributes (Column Names) in the CSV File:")
        #for attr in attributes:
            #print(f"- {attr}")

        # Use dictionary for ages in increasing age
        race_ethnicities = {}
        for race in data[race_col]:
            if isinstance(race, str):
                race = race.strip()
                if race in race_ethnicities:
                    race_ethnicities[race] += 1
                else:
                    race_ethnicities[race] = 1

        race_ethnicities = dict(sorted(race_ethnicities.items()))

        #print("\nNumber of Patients by Race and Ethnicity Combined")
        #print(race_ethnicities)

        return race_ethnicities

    except FileNotFoundError:
        print(f"Error: File not found at {covid_file}. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

covid_file = "COVIDData.csv"
raceEthnicityCount(covid_file)