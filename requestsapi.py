import requests
import os

def upload_file(file_path):
    """Upload a file to the server."""

    url = "http://localhost:5000/upload"
    files = {"file": open(file_path, "rb")}

    response = requests.post(url, files=files)

    if response.status_code == 200:
        file_id = response.json()["file_id"]
        return file_id
    else:
        raise Exception("Failed to upload file: {}".format(response.content))

def fetch_file(file_id):
    """Fetch a file from the server."""

    url = "http://localhost:5000/fetch?file_id={}".format(file_id)
    response = requests.get(url)

    if response.status_code == 200:
        file_content = response.content
        return file_content
    else:
        raise Exception("Failed to fetch file: {}".format(response.content))

def consolidate_files(file_ids):
    """Consolidate all uploaded files into a single file."""

    url = "http://localhost:5000/consolidate"

    files = {}
    for i, file_id in enumerate(file_ids):
        files["file_{}".format(i)] = fetch_file(file_id)

    response = requests.post(url, files=files)

    if response.status_code == 200:
        consolidated_file_content = response.content
        return consolidated_file_content
    else:
        raise Exception("Failed to consolidate files: {}".format(response.content))

if __name__ == "__main__":
    # Upload some files
    file_id_1 = upload_file("myfile1.txt")
    file_id_2 = upload_file("myfile2.txt")

    # Fetch the files
    file_content_1 = fetch_file(file_id_1)
    file_content_2 = fetch_file(file_id_2)

    # Consolidate the files
    consolidated_file_content = consolidate_files([file_id_1, file_id_2])

    # Save the consolidated file
    with open("consolidated_file.txt", "wb") as f:
        f.write(consolidated_file_content)
