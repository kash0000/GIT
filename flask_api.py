from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

# Upload a file
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file_id = generate_file_id()
    file_path = os.path.join("uploads", file_id)

    file.save(file_path)

    return jsonify({"file_id": file_id})

# Fetch a file
@app.route("/fetch", methods=["GET"])
def fetch_file():
    file_id = request.args.get("file_id")
    file_path = os.path.join("uploads", file_id)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"})

    return send_file(file_path)

# Consolidate all uploaded files
@app.route("/consolidate", methods=["GET"])
def consolidate_files():
    files = []
    for file_id in os.listdir("uploads"):
        file_path = os.path.join("uploads", file_id)

        with open(file_path, "rb") as f:
            file_content = f.read()

        files.append(file_content)

    consolidated_file = b"".join(files)

    return send_file(consolidated_file, mimetype="application/octet-stream", as_attachment=True)

# Generate a random file ID
def generate_file_id():
    import random
    return str(random.randint(1000000000, 9999999999))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
