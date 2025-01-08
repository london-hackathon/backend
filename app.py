from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os

#Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# Allow requests only from localhost:3000 for development
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/api/bias', methods=['POST'])
def analysis_endpoint():
    try:
        # Check if the request has a file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']  # Get the uploaded CSV file
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Get demographic and description from the form data
        demographic = request.form.get('demographic')
        description = request.form.get('description')

        if not demographic or not description:
            return jsonify({'error': 'Demographic and description are required'}), 400

        # Log the received data for debugging
        logging.debug(f"Received demographic: {demographic}")
        logging.debug(f"Received description: {description}")
        logging.debug(f"Received file: {file.filename}")

        # Perform your processing here (e.g., saving the file, processing data)
        result = {
            'message': 'Data received successfully',
            'demographic': demographic,
            'description': description,
            'filename': file.filename
        }

        # Return a success response
        return jsonify(result), 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")  # Log the error for debugging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port)