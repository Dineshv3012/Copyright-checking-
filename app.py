from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'media' not in request.files:
        return 'No file part'
    file = request.files['media']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        # Fake copyright check
        if "copyright" in filename.lower():
            return "❌ Copyrighted content detected!"
        return "✅ No copyright detected (placeholder result)"
    return 'Error in upload'

if __name__ == '__main__':
    app.run(debug=True)