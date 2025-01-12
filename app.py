
from flask import Flask, request
import os

# Load the lookup table (this would be your emulated face recognition model)
lookup_table = {}
with open('classification_face_images_1000.csv', 'r') as f:
    for line in f:
        filename, result = line.strip().split(',')
        lookup_table[filename] = result

app = Flask(__name__)

@app.route("/", methods=["POST"])
def face_recognition():
    # Retrieve the uploaded image from the POST request
    if "inputFile" not in request.files:
        return "No file part", 400
    
    file = request.files["inputFile"]
    filename = file.filename.split('.')[0]
    print(filename)
    
    # Use the lookup table to find the corresponding prediction result
    prediction_result = lookup_table.get(filename, "Unknown")
    
    # Return the result in the required format
    return f"{filename}:{prediction_result}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
