from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os
from gender_count import count_gender  # Import gender counting function
from analyze_bias import analyze_bias  # Import bias analysis function
from age_count import count_age  # Import age counting function
from race_count import raceEthnicityCount  # Import race/ethnicity counting function

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# Allow requests only from localhost:3000 for development
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/api/bias', methods=['POST'])
def analysis_endpoint():
    try:
        # Check if the request contains a file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Get demographic and description from the form data
        demographic = request.form.get('demographic')
        description = request.form.get('description')

        if not demographic or not description:
            return jsonify({'error': 'Demographic and description are required'}), 400

        # Save the uploaded file temporarily
        file_path = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)  # Ensure the uploads directory exists
        file.save(file_path)

        # Call the appropriate function based on the demographic
        if demographic.lower() in ["gender", "sex"]:
            # Gender demographic processing
            gender_data = count_gender(file_path, "Sex")
            if "error" in gender_data:
                return jsonify(gender_data), 400
            processed_data = gender_data

        elif demographic.lower() == "age":
            # Age demographic processing
            age_data = count_age(file_path)
            if "error" in age_data:
                return jsonify(age_data), 400
            processed_data = age_data

        elif demographic.lower() in ["race", "ethnicity"]:
            # Race/Ethnicity demographic processing
            race_ethnicity_data = raceEthnicityCount(file_path)
            if "error" in race_ethnicity_data:
                return jsonify(race_ethnicity_data), 400
            processed_data = race_ethnicity_data

        else:
            return jsonify({'error': f"Unsupported demographic: {demographic}"}), 400

        # Call the analysis function
        explanation, score = analyze_bias(processed_data, description, demographic)

        # Return the results to the frontend
        result = {
            "explanation": explanation,
            "score": score,
            "demographic": demographic,
            "processed_data": processed_data,
            "description": description
        }
        return jsonify(result), 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
