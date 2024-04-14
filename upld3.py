import os
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = 'backend/uploads'  # Specify the upload directory

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        # Create the upload directory if it does not exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Save the uploaded file to the upload directory
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process the uploaded file
        data = pd.read_excel(file_path)
        
        # Process data here
        
        # Save processed data to a new file
        processed_file_path = os.path.join(UPLOAD_FOLDER, 'processed_data.xlsx')
        data.to_excel(processed_file_path, index=False)
        
        return jsonify({'message': 'File uploaded and processed successfully', 'file_path': processed_file_path})
    else:
        return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    app.run(debug=True)
