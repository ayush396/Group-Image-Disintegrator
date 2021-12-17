from flask import Flask,render_template,send_file,request
import os
from extrator import extract
from werkzeug.utils import secure_filename

from seperator import seperate
from insight import Female,Male
import shutil

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
        seperate.segregator()
        shutil.make_archive('env\segregatorMale','zip','env\Male')
        shutil.make_archive('env\segregatorFemale','zip','env\Female')
        Female.helper()
        Male.helper()
        return render_template("upload.html")

@app.route('/download')
def segregatorMale():
    p='segregatorMale.zip'
    return send_file(p,as_attachment=True)

@app.route('/downloadF')
def segregatorFemale():
    p='segregatorFemale.zip'
    return send_file(p,as_attachment=True)

@app.route('/insights')
def insights():
    return render_template('insight.html')

if __name__ == '__main__':
    app.run(debug=True)
