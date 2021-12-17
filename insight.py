import os 
import cv2
from PIL import Image
import numpy as np
import shutil

files=os.listdir('env//female')
print(files)
files2=os.listdir('env//male')
shutil.rmtree('env//border')
os.mkdir('env//border')
shutil.rmtree('env//border2')
os.mkdir('env//border2')

for i in files:
    im = cv2.imread('env//female//'+i)
    border = cv2.copyMakeBorder(
    im, 7, 7, 7, 7, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    cv2.imwrite('env//border//output_'+ i , border)

    border_files=os.listdir('env//border')

for i in files2:
    im = cv2.imread('env//male//'+i)
    border = cv2.copyMakeBorder(
    im, 7, 7, 7, 7, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    cv2.imwrite('env//border2//output_'+ i , border)

    border_files2=os.listdir('env//border2')

def evenFemale():
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
        if len(border_files)%2==0:
            evenFemale()
        else:
            oddFemale()
class Male():
    def __init__(self) :
        pass
    def helper():
        if len(border_files2)%2==0:
            evenMale()
        else:
            oddMale()