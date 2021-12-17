import os 
import cv2
from PIL import Image
import numpy as np
import shutil

def evenFemale():
    border_files=os.listdir('env//border')

    img_count=[]
    for x in border_files:
        img=Image.open('env//border//'+x)
        img1_array = np.array(img)
        img_count.append(img)

    hStack=[]
    for i in range(0,len(img_count),2):
        hStack.append(np.hstack([img_count[i] , img_count[i+1]]))

    final=np.vstack([h for h in hStack])
    collage=Image.fromarray(final)

    collage.save("env//static//collage.jpg")
    print("image saved")


def oddFemale():
    border_files=os.listdir('env//border')
    img_count=[]
    for x in border_files:
        img=Image.open('env//border//'+x)
        img1_array = np.array(img)
        img_count.append(img)

    hStack=[]
    for i in range(0,len(img_count)-1,2):
        hStack.append(np.hstack([img_count[i] , img_count[i+1]]))

    yet_final=np.vstack([h for h in hStack])

    y=cv2.imread('env//border//'+border_files[-1])
    y=cv2.cvtColor(y,cv2.COLOR_BGR2RGB)
    print(border_files[-1])
    y=cv2.resize(y,(388,482))
    final=np.vstack([y,yet_final])
    collage=Image.fromarray(final)

    collage.save("env//static//collage.jpg")
    print("image saved")


def evenMale():
    border_files2=os.listdir('env//border2')
    img_count=[]
    for x in border_files2:
        img=Image.open('env//border2//'+x)
        img1_array = np.array(img)
        img_count.append(img)

    hStack=[]
    for i in range(0,len(img_count),2):
        hStack.append(np.hstack([img_count[i] , img_count[i+1]]))

    final=np.vstack([h for h in hStack])
    collage=Image.fromarray(final)

    collage.save("env//static//collage2.jpg")
    print("image saved")


def oddMale():
    border_files2=os.listdir('env//border2')
    img_count=[]
    for x in border_files2:
        img=Image.open('env//border2//'+x)
        img1_array = np.array(img)
        img_count.append(img)

    hStack=[]
    for i in range(0,len(img_count)-1,2):
        hStack.append(np.hstack([img_count[i] , img_count[i+1]]))

    yet_final=np.vstack([h for h in hStack])

    y=cv2.imread('env//border2//'+border_files2[-1])
    y=cv2.cvtColor(y,cv2.COLOR_BGR2RGB)
   
    y=cv2.resize(y,(388,482))
    final=np.vstack([y,yet_final])
    collage=Image.fromarray(final)

    collage.save("env//static//collage2.jpg")
    print("image saved")


class Female():
    def __init__(self):
        pass

    def helper():
        border_files=os.listdir('env//border')
        if len(border_files)%2==0:
            if len(border_files)==0:
                img = Image.open('env//static//female.jpg')
                img = img.convert("RGB")
                 
                img.save('env//static//collage.jpg',format='JPEG', quality=95)
            else:
                evenFemale()
        else:
            if len(border_files)==1:
                img=Image.open('env//border//'+border_files[0])
                img.save('env//static//collage.jpg')
            else:
                oddFemale()
class Male():
    def __init__(self) :
        pass
    def helper():
        border_files2=os.listdir('env//border2')
        if len(border_files2)%2==0:
            if len(border_files2)==0:
                img = Image.open('env//static//male.jpg')
                img = img.convert("RGB")
    
                img.save('env//static//collage2.jpg',format='JPEG', quality=95)
            else:
                evenMale()
        else:
            if len(border_files2)==1:
                img=Image.open('env//border2//'+border_files2[0])
                img.save('env//static//collage2.jpg')
            else:
                oddMale()
