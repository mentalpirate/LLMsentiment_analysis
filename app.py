import os 
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import secrets
import pyanalysis as pyans
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
SECRET_KEY = secrets.token_hex()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

@app.route('/')
def home():
    return "Hello World"

def allowed_file(filename):
     return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

#Show status as processing till it is finished
@app.route('/processing')
def process():
    return outfile


@app.route('/upload',methods=["GET","POST"])
def file_upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            print("No file part")
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            print("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            global outfile
            filename = secure_filename(file.filename)
            print("file uploaded successfully")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("Processing the file please wait")
            print(filename)
            outfile = pyans.generate_analysis(filename)
            #return redirect(url_for('download_file', name=filename))
            return redirect(url_for('process'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
if __name__ == '__main__':
    app.run(debug=True)