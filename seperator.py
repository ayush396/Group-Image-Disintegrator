import os
import cv2
import numpy as np

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


model=load_model('env\GenderClassifier.model')
prediction=[]
allfiles=[]

classes=['Male','Female']
#print(input[8])


class seperate():
    def __init__(self):
        pass
    
    def segregator():
        input=os.listdir('env//extracted_pics')
        # files=os.listdir('env//extracted_pics')
        for x in input:
            img=cv2.imread('env//extracted_pics//'+x)
            print(x)
            img=cv2.resize(img,(96,96))
            img=img.astype('float')/255.0

            img=img_to_array(img)
            img=np.expand_dims(img,axis=0)

            pred=model.predict(img)[0]
            #print(pred[0])
            if pred[0]>0.5:
                idx=0
            else:
                idx=1
            label=classes[idx]
            prediction.append(label)
                 
            #print(prediction)
            
            #print(files)


            # print(len(prediction))
            for i in range(len(prediction)):
                if prediction[i]=='Female':
                    im=cv2.imread('env//extracted_pics//'+input[i])
                    path='env//Female//'+input[i]
                    cv2.imwrite(path,im)
                    border = cv2.copyMakeBorder(im, 7, 7, 7, 7, cv2.BORDER_CONSTANT, value=[255, 255, 255])
                    cv2.imwrite('env//border//output_'+ input[i] , border)

                else:
                    img=cv2.imread('env//extracted_pics//'+input[i])
                    path='env//Male//'+input[i]
                    cv2.imwrite(path,img)
                    border = cv2.copyMakeBorder(img, 7, 7, 7, 7, cv2.BORDER_CONSTANT, value=[255, 255, 255])
                    cv2.imwrite('env//border2//output_'+ input[i] , border)

     
        print(len(prediction))








    


      
