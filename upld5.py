import xlsxwriter

def read_xlsb_sheet(file_path, sheet_name, columns):
    with pyxlsb.open_workbook(file_path) as wb:
        with wb.get_sheet(sheet_name) as sheet:
            rows = []
            for i, row in enumerate(sheet.rows()):
                if i >= 5:  # Skip first 6 rows (0-based index)
                    rows.append([cell.v for cell in row])

    df = pd.DataFrame(rows[1:], columns=rows[0])  # Assuming first row contains column headers
    return df[columns]  # Select only specified columns

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        # Create the upload directory if it does not exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Save the uploaded file to the upload directory
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Specify columns to extract data from
        original_columns = ['Owning transaction cycle id', 'IT business service name', 'CI count', 'Incident count']
        processed_columns = ['Transaction ID', 'Service Name', 'CI Count', 'Incident Count']

        # Process the uploaded file
        data = read_xlsb_sheet(file_path, sheet_name='Sheet1', columns=original_columns)
        
        # Rename columns
        data.columns = processed_columns

        # Save processed data to a new file with original filename and suffix '_processed'
        processed_file_name = os.path.splitext(file.filename)[0] + '_processed.xlsx'
        processed_file_path = os.path.join(UPLOAD_FOLDER, processed_file_name)

        # Write to Excel using xlsxwriter engine with currency format
        with pd.ExcelWriter(processed_file_path, engine='xlsxwriter') as writer:
            data.to_excel(writer, index=False, sheet_name='Sheet1')
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            currency_format = workbook.add_format({'num_format': '£#,##0.00'})
            for col_num, col_name in enumerate(processed_columns):
                if 'Count' not in col_name:  # Apply currency format only to columns other than 'Count'
                    worksheet.set_column(col_num, col_num, cell_format=currency_format)

        return jsonify({'message': 'File uploaded and processed successfully', 'file_path': processed_file_path})
    else:
        return jsonify({'error': 'No file uploaded'})
