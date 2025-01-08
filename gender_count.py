import pandas as pd

def count_gender(file_path, gender_column):
    """
    Counts the number of males and females in a given CSV file.

    Args:
        file_path (str): The path to the CSV file.
        gender_column (str): The column name containing gender data.

    Returns:
        dict: A dictionary with counts for 'Male' and 'Female'.
    """
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Check if the specified column exists
        if gender_column not in data.columns:
            return {"error": f"'{gender_column}' column not found in the file."}
        
        # Map numerical or string gender values to 'Male' and 'Female'
        gender_mapping = {
            1: 'Male', 0: 'Female',  # Common numerical encoding
            'Male': 'Male', 'Female': 'Female',  # String encoding
            'M': 'Male', 'F': 'Female'  # Short string encoding
        }

        # Normalize gender values using the mapping
        data['NormalizedGender'] = data[gender_column].map(gender_mapping)

        # Count the occurrences of each gender
        gender_counts = data['NormalizedGender'].value_counts()

        # Create the result dictionary and cast values to int
        result = {
            "Male": int(gender_counts.get('Male', 0)),
            "Female": int(gender_counts.get('Female', 0))
        }

        return result
    except Exception as e:
        return {"error": str(e)}
