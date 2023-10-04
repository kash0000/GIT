from fastapi import FastAPI, File, UploadFile
import pandas as pd
from typing import List, Dict

app = FastAPI()

@app.post("/excel-to-json")
async def excel_to_json(files: List[UploadFile]):
    # Check if files were uploaded
    if not files:
        return {"error": "No files were uploaded"}

    # Initialize an empty list to store JSON data
    json_data_list = []

    for file in files:
        # Check if the file has an allowed extension (e.g., .xlsx)
        allowed_extensions = {'xlsx', 'xls'}
        if file.filename.split('.')[-1].lower() not in allowed_extensions:
            return {"error": "Invalid file extension"}

        # Read the Excel file into a DataFrame
        try:
            df = pd.read_excel(file.file)
        except Exception as e:
            return {"error": "Failed to read Excel file", "details": str(e)}

        # Convert the DataFrame to JSON and append it to the list
        json_data = df.to_dict(orient='records')
        json_data_list.append({file.filename: json_data})

    return json_data_list

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
