import pandas as pd

cardio_file = "CardioData.csv"
# Age: Age of the patient
# Sex: Gender of the patient (0 = Female, 1 = Male)

try:
    # Read the CSV file
    data = pd.read_csv(cardio_file)

    # Get column names (attributes)
    attributes = list(data.columns)
    # Print the attributes
    print("Attributes (Column Names) in the CSV File:")
    for attr in attributes:
        print(f"- {attr}")

    male_count = 0
    female_count = 0

    for sex in data['Sex']:
        if sex == 1:  # Male
            male_count += 1
        elif sex == 0:  # Female
            female_count += 1

    # Use dictionary for ages in increasing age
    age_count = {}
    for age in data['Age']:
        if age in age_count:
            age_count[age] += 1
        else:
            age_count[age] = 1

    sorted_age = dict(sorted(age_count.items()))

    print("\nNumber of Patients by age")
    print(sorted_age)

    print("Number of patients by gender")
    print("Male (1): ", male_count)
    print("Female (0): ", female_count)



    #----------------------------------------------------------------------------------
    # Pandas stuff (aka actual count)
    print("\n\n\n\n\nPandas stuff (aka actual count)")
    age_count = data['Age'].value_counts().sort_index()
    gender_count = data['Sex'].value_counts()

    print("Number of patients by age:")
    print(age_count)

    print("\nNumber of patients by gender: 0 for female and 1 for male")
    print(gender_count)
    
except FileNotFoundError:
    print(f"Error: File not found at {cardio_file}. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")