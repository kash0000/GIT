import os
import pandas as pd
import sqlite3

# Define constants
PROCESSED_FILE_PATH = 'C:/users/xyz/documents/processed/processed_data.xlsx'
DATABASE_PATH = 'C:/users/xyz/documents/backend/tcoDb.db'
TABLE_NAME = 'TCO_MASTER'

def import_processed_file_into_db():
    conn = None
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        # Read the processed file into a DataFrame
        data_frame = pd.read_excel(PROCESSED_FILE_PATH)

        # Ensure that the 'MonthEnd' column exists and extract its first value
        if 'MonthEnd' not in data_frame.columns:
            raise KeyError("The 'MonthEnd' column is missing from the processed file.")
        month_end = data_frame['MonthEnd'].iloc[0]

        # Delete existing records for the particular 'MonthEnd'
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE MonthEnd = ?", (month_end,))

        # Insert the data into the database
        data_frame.to_sql(TABLE_NAME, conn, if_exists='append', index=False)

        # Commit the changes
        conn.commit()
        print("Data imported successfully into TCO_MASTER table.")
    except Exception as e:
        print(f"Error importing data into TCO_MASTER table: {e}")
    finally:
        # Close the connection if it's not None
        if conn is not None:
            conn.close()

# Example usage: calling the function directly
import_processed_file_into_db()
