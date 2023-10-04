from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/excel-to-json', methods=['POST'])
def excel_to_json():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file has an allowed extension (e.g., .xlsx)
    allowed_extensions = {'xlsx', 'xls'}
    if file.filename.split('.')[-1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file extension'})

    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(file)
    except Exception as e:
        return jsonify({'error': 'Failed to read Excel file', 'details': str(e)})

    # Convert the DataFrame to JSON
    json_data = df.to_json(orient='records')

    return jsonify({'data': json_data})

if __name__ == '__main__':
    app.run(debug=True)
