from flask import Flask,render_template,send_file,request
import os
from extrator import extract
from werkzeug.utils import secure_filename

from seperator import seperate
from insight import Female,Male
import shutil
import cv2

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
        im=cv2.imread('env//static//upload.jpg')
        ans=im.shape
        f=os.listdir('env//extracted_pics')
        val=len(f)
        f1=os.listdir('env//Male')
        val1=len(f1)
        f2=os.listdir('env//Female')
        val2=len(f2)
        return render_template("insight.html",ans1=ans[0],ans2=ans[1],val=val,val1=val1,val2=val2)

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
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
