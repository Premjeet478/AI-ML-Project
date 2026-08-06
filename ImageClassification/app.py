from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from app_helper import get_classes

app = Flask(__name__)

# Upload folder ka path set karna
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    # Ye home page (index.html) dikhayega jahan upload button hai
    return render_template("index.html")

@app.route("/uploader", methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        
        # Photo ko safe karke save karna
        filename = secure_filename(f.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(path)
        
        # AI prediction logic (app_helper.py se)
        result = get_classes(path)
        
        # Result ko screen par dikhana
        return f"<h1>Prediction: {result}</h1><br><a href='/'>Upload Another</a>"

if __name__ == "__main__":
    # CloudxLab ke liye port 8080 ya 4100-4140 ke beech ka port zaroori hai
    app.run(host='0.0.0.0', port=4100)