from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/first")
def hello():
  return {"Hello world!"}
# ==============================================================
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/get-iris")
# def get_iris():

#     import pandas as pd
#     url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
#     iris = pd.read_csv(url)

#     return iris
# ==========================================================================

# main.py
# pip install python-multipart

# from fastapi import FastAPI, File, UploadFile
# import os

# import uvicorn

# app = FastAPI()

# # Upload a file
# @app.post("/upload")
# async def upload_file(file: UploadFile):
#     file_id = generate_file_id()
#     file_path = os.path.join("uploads", file_id)

#     await file.save(file_path)

#     return {"file_id": file_id}

# # Fetch a file
# @app.get("/fetch")
# async def fetch_file(file_id: str):
#     file_path = os.path.join("uploads", file_id)

#     if not os.path.exists(file_path):
#         return {"error": "File not found"}

#     with open(file_path, "rb") as f:
#         file_content = f.read()

#     return {"file_content": file_content}

# # Consolidate all uploaded files
# @app.get("/consolidate")
# async def consolidate_files():
#     files = []
#     for file_id in os.listdir("uploads"):
#         file_path = os.path.join("uploads", file_id)

#         with open(file_path, "rb") as f:
#             file_content = f.read()

#         files.append(file_content)

#     consolidated_file = b"".join(files)

#     return {"consolidated_file": consolidated_file}

# # Generate a random file ID
# def generate_file_id():
#     import random
#     return str(random.randint(1000000000, 9999999999))

if __name__ == "__main__":
    uvicorn.run(app, port=3100)

# host="0.0.0.0"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from pydantic import BaseModel, ValidationError


# class Model(BaseModel):
#     x: str


# try:
#     Model()
# except ValidationError as exc:
#     print(repr(exc.errors()[0]['type']))
#     #> 'missing'
