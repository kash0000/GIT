import os
import sqlite3
from flask import Flask, request, jsonify
import openpyxl  # Use openpyxl for Excel file processing

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Connect to SQLite3 database (replace with your connection details)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'excelFile' not in request.files:
        return jsonify({'message': 'No file uploaded.'}), 400

    file = request.files['excelFile']
    filename = secure_filename(file.filename)  # Sanitize filename for security
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    try:
        workbook = openpyxl.load_workbook(os.path.join(UPLOAD_FOLDER, filename))
        sheet = workbook.active

        # Select only the required columns by name (adjust names as needed)
        required_columns = ['ColumnA', 'ColumnC']  # Replace with your column names
        data = []
        for row in sheet.iter_rows():
            filtered_row = [cell.value for cell in row if cell.value in required_columns]
            if filtered_row:  # Only include rows with at least one desired column value
                data.append(filtered_row)

        # Dynamically build the INSERT statement based on selected columns
        column_names = ', '.join(required_columns)
        placeholders = ', '.join(['?'] * len(required_columns))
        insert_stmt = f'INSERT INTO your_table_name ({column_names}) VALUES ({placeholders})'

        cursor.executemany(insert_stmt, data)
        conn.commit()

        return jsonify({'message': 'Excel file uploaded and processed successfully.'})

    except Exception as e:
        return jsonify({'message': 'Error processing Excel file: ' + str(e)}), 500

    finally:
        os.remove(os.path.join(UPLOAD_FOLDER, filename))  # Delete the temporary file

if __name__ == '__main__':
    app.run(debug=True)  # Adjust for production environment
