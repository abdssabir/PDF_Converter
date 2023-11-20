from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Save the uploaded file to a known location
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Run the script with the uploaded file path
    subprocess.run(['python', 'script.py', file_path])

    return 'File uploaded and script executed successfully'

if __name__ == '__main__':
    app.run(debug=True)
