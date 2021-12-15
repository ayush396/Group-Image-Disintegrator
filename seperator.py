import os
import cv2
import numpy as np

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import shutil

model=load_model('env\GenderClassifier.model')
prediction=[]
input=os.listdir('env//extracted_pics')


classes=['Male','Female']
#print(input[8])


class seperate():
    def __init__(self):
        pass
    
    def segregator():
        shutil.rmtree('env//Female')
        shutil.rmtree('env//Male')
        os.mkdir('env//Male')
        os.mkdir('env//Female')
        for x in input:
            img=cv2.imread('env//extracted_pics//'+x)
            img=cv2.resize(img,(96,96))
            img=img.astype('float')/255.0

            img=img_to_array(img)
            img=np.expand_dims(img,axis=0)

            pred=model.predict(img)[0]
            #print(pred[0])
            if pred[0]>0.95:
                idx=0
            else:
                idx=1
            label=classes[idx]
            prediction.append(label)

            #print(prediction)
            

            # print(len(prediction))
            for i in range(len(prediction)):
                if prediction[i]=='Female':
                    im=cv2.imread('env//extracted_pics//'+input[i])
                    path='env//Female//'+input[i]
                    cv2.imwrite(path,im)
                else:
                    img=cv2.imread('env//extracted_pics//'+input[i])
                    path='env//Male//'+input[i]
                    cv2.imwrite(path,img)