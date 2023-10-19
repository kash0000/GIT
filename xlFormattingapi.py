pip install flask pandas openpyxl

from flask import Flask, request, jsonify
import pandas as pd
from ml_model import your_ml_function  # Import your ML model function

app = Flask(__name)

@app.route('/process_excel', methods=['POST'])
def process_excel():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    # Check if the file is in the right format
    if file.filename == '':
        return "No selected file", 400
    if not file.filename.endswith('.xlsx'):
        return "Invalid file format, please upload an Excel file (.xlsx)", 400

    try:
        # Read the uploaded Excel file
        df = pd.read_excel(file, engine='openpyxl')

        # Iterate through the rows and create the formatted strings
        formatted_strings = []
        for index, row in df.iterrows():
            amount = row['Amount']
            pl = row['PL']
            pe_balance = row['pe_balance']
            formatted_string = f'#Amount#: {amount} #PL#: {pl} #pe_balance#:{pe_balance}'
            formatted_strings.append(formatted_string)

        # Join the formatted strings with line breaks
        result = '\n'.join(formatted_strings)

        # Send the formatted string to your ML model function
        ml_result = your_ml_function(result)

        # You can return the ML model's result as JSON or any other format
        return jsonify({"ml_result": ml_result})
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
