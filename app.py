from flask import Flask,render_template,request
import os
from extrator import extract
from werkzeug.utils import secure_filename
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['inp_file']
        f.save(os.path.join("env//static",secure_filename('upload.jpg')))
        extract.faces()
        return "Upload Successfully"
    
if __name__ == '__main__':
    app.run(debug=True)
