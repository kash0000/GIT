#file-upload.component.ts:

import { Component } from '@angular/core';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent {

  constructor(private fileUploadService: FileUploadService) { }

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    this.fileUploadService.uploadFile(file).subscribe(
      (response) => {
        console.log('File uploaded successfully:', response);
      },
      (error) => {
        console.error('Error uploading file:', error);
      }
    );
  }
}

#file-upload.service.ts:

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FileUploadService {

  constructor(private http: HttpClient) { }

  uploadFile(file: File) {
    const formData = new FormData();
    formData.append('file', file);

    return this.http.post<any>('http://your-backend-url/upload', formData);
  }
}


#python 

  from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    data = pd.read_excel(file)
    
    # Process data here
    
    # Save processed data to a new file
    processed_file_path = 'processed_data.xlsx'
    data.to_excel(processed_file_path, index=False)
    
    return jsonify({'message': 'File uploaded and processed successfully', 'file_path': processed_file_path})

if __name__ == '__main__':
    app.run(debug=True)


#python1

//   from sqlalchemy import create_engine
// import pandas as pd

// engine = create_engine('your-database-connection-string')

// data = pd.read_excel('processed_data.xlsx')
// data.to_sql('your_table_name', engine, if_exists='append', index=False)


  import sqlite3

def import_processed_file_into_db(file_path):
    # Connect to the database
    conn = sqlite3.connect('backend/tcoDb.db')
    cursor = conn.cursor()

    try:
        # Delete existing records for the particular 'MonthEnd' if needed
        # Execute appropriate DELETE command here if required

        # Import processed data from the file into the database
        query = f"DELETE FROM TCO_MASTER WHERE MonthEnd = (SELECT MonthEnd FROM {file_path})"
        cursor.execute(query)
        query = f".mode csv\n.import {file_path} TCO_MASTER"
        cursor.execute(query)

        # Commit the changes
        conn.commit()
        print("Data imported successfully into TCO_MASTER table.")
    except Exception as e:
        print("Error importing data into TCO_MASTER table:", e)
    finally:
        # Close the connection
        conn.close()

