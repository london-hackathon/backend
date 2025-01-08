import pandas as pd

def count_age(file):
    try:
        # Read the CSV file
        data = pd.read_csv(file)

        # Get column names (attributes)


        # Use dictionary for ages in increasing age
        #buckets increment 0-9, 10-19, 90+
        age_count = {}
        for age in data['Age']:
            val = age//10
            if val >= 9:
                age_count[9] += 1
            else:
                if val in age_count:
                    age_count[val] += 1
                else:
                    age_count[val] = 1

        sorted_age = dict(sorted(age_count.items()))
        sorted_age_modified = {}
        for x,y in sorted_age.items():
            if x == 9:
                str_key = "90+"
            else:
                str_key = str(x*10) + "-" + str(x*10+9)
            sorted_age_modified[str_key] = y

        print("\nNumber of Patients by age")
        print(sorted_age_modified)


        #----------------------------------------------------------------------------------
        # Pandas stuff (aka actual count)
        print("\n\n\n\n\nPandas stuff (aka actual count)")
        #age_count = data['Age'].value_counts().sort_index()
        #gender_count = data['Sex'].value_counts()

        print("Number of patients by age:")
        print(age_count)

        '''print("\nNumber of patients by gender: 0 for female and 1 for male")
        print(gender_count)'''
        
    except FileNotFoundError:
        print(f"Error: File not found at {file}. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

