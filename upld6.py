from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def read_xlsb_sheet(file_path, sheet_name, columns):
    with pyxlsb.open_workbook(file_path) as wb:
        with wb.get_sheet(sheet_name) as sheet:
            rows = []
            for i, row in enumerate(sheet.rows()):
                if i >= 5:  # Skip first 6 rows (0-based index)
                    row_data = [cell.v for cell in row]
                    if row_data[0]:  # Check if 'Owning transaction cycle Id' is not blank
                        rows.append(row_data)

    # Give a distinctive name to the DataFrame
    data_frame = pd.DataFrame(rows[1:], columns=rows[0])  # Assuming first row contains column headers
    return data_frame[columns]  # Select only specified columns

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
        data_frame = read_xlsb_sheet(file_path, sheet_name='Sheet1', columns=original_columns)
        
        # Specify columns to extract data from
        original_columns = ['Owning transaction cycle id', 'IT business service name', 'CI count', 'Incident count']
        processed_columns = ['MonthEnd'] + original_columns

        # Extract month and year from the filename
        month, year = extract_month_year(file.filename)

        if month and year:
            # Create new 'MonthEnd' column with extracted month and year in date format
            month_end_date = pd.to_datetime(f'{month} {year}', format='%b %Y')
            # Repeat the same month and year for all rows in the DataFrame
            month_end_column = [month_end_date.strftime('%d-%m-%Y')] * len(data_frame)
        else:
            # If extraction fails, fill the 'MonthEnd' column with NaN values
            month_end_column = [np.nan] * len(data_frame)
        
        # Add 'MonthEnd' column to the DataFrame
        data_frame['MonthEnd'] = month_end_column

        # Create a new workbook
        wb = Workbook()
        ws = wb.active

        # Write data frame to worksheet
        for r_idx, row in enumerate(dataframe_to_rows(data_frame, index=False, header=True)):
            for c_idx, value in enumerate(row):
                ws.cell(row=r_idx+1, column=c_idx+1, value=value)

        # Save processed data to a new file with original filename and suffix '_processed'
        processed_file_name = os.path.splitext(file.filename)[0] + '_processed.xlsx'
        processed_file_path = os.path.join(UPLOAD_FOLDER, processed_file_name)

        # Save workbook to file
        wb.save(processed_file_path)

        return jsonify({'message': 'File uploaded and processed successfully', 'file_path': processed_file_path})
    else:
        return jsonify({'error': 'No file uploaded'})

==================================================================
FILE UPLOAD's
++html++

<div class="upload-container">
  <label for="fileInput" class="custom-file-upload">
    Choose File
    <input type="file" id="fileInput" (change)="onFileSelected($event)" />
  </label>
  <div class="loading-bar" [hidden]="!uploading">
    <!-- Loading bar content -->
  </div>
</div>
===================================================================
++css++

.upload-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.custom-file-upload {
  display: inline-block;
  padding: 10px 20px;
  cursor: pointer;
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
}

.loading-bar {
  margin-top: 20px;
  width: 200px;
  height: 10px;
  background-color: #ccc;
  border-radius: 5px;
}

.loading-bar-inner {
  width: 0;
  height: 100%;
  background-color: #007bff;
  border-radius: 5px;
  transition: width 0.3s ease-in-out;
}

===========================================
++ ts++
export class FileUploadPageComponent {
  uploading: boolean = false;

  onFileSelected(event) {
    this.uploading = true;
    // Perform file upload logic here

    // Simulating file upload completion after 3 seconds (replace with actual upload logic)
    setTimeout(() => {
      // Set uploading back to false after upload is complete
      this.uploading = false;
    }, 3000);
  }
}



