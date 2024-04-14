import os
from flask import Flask, request, jsonify
import pandas as pd
import pyxlsb

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
        data = read_xlsb_sheet(file_path, sheet_name='Sheet1', column_name='IT Business Service Name')
        
        # Save processed data to a new file with original filename and suffix '_processed'
        processed_file_name = os.path.splitext(file.filename)[0] + '_processed.xlsx'
        processed_file_path = os.path.join(UPLOAD_FOLDER, processed_file_name)
        data.to_excel(processed_file_path, index=False)
        
        return jsonify({'message': 'File uploaded and processed successfully', 'file_path': processed_file_path})
    else:
        return jsonify({'error': 'No file uploaded'})

def read_xlsb_sheet(file_path, sheet_name, column_name):
    with pyxlsb.open_workbook(file_path) as wb:
        with wb.get_sheet(sheet_name) as sheet:
            rows = []
            for row in sheet.rows():
                rows.append([cell.v for cell in row])

    df = pd.DataFrame(rows[1:], columns=rows[0])  # Assuming first row contains column headers
    return df[[column_name]]

if __name__ == '__main__':
    app.run(debug=True)
