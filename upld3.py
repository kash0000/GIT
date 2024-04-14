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
        
        # Select only 'source_name' and 'project_name' columns
        processed_data = data[['source_name', 'project_name']]

        # Save processed data to a new file with original filename and suffix '_processed'
        processed_file_name = os.path.splitext(file.filename)[0] + '_processed.xlsx'
        processed_file_path = os.path.join(UPLOAD_FOLDER, processed_file_name)
        processed_data.to_excel(processed_file_path, index=False)
        
        return jsonify({'message': 'File uploaded and processed successfully', 'file_path': processed_file_path})
    else:
        return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    app.run(debug=True)


=====================
6. Load Data into Database
Use a database library like SQLAlchemy or psycopg2 to load data from the processed file into your database. Here's a basic example using SQLAlchemy:

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('your-database-connection-string')

data = pd.read_excel('processed_data.xlsx')
data.to_sql('your_table_name', engine, if_exists='append', index=False)

