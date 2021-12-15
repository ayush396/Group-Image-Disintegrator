from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam 
from tensorflow.keras.preprocessing.image import img_to_array

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import BatchNormalization,Conv2D,MaxPooling2D
from tensorflow.keras.layers import Activation,Flatten,Dropout,Dense

from tensorflow.keras import backend

import cv2
import random

import numpy as np
import os
import glob
from sklearn.model_selection import train_test_split

data=[]
name=[]
epochs=50
img_dims=(96,96,3)

img_files=[img for img in glob.glob(r'env//gender_dataset'+'/**/*',recursive=True) if not os.path.isdir(img)]
#print(img_files)

random.shuffle(img_files)

for x in img_files:
    image=cv2.imread(x)
    image=cv2.resize(image,(96,96))
    image=img_to_array(image)

    data.append(image)
    gender=x.split(os.path.sep)[-2]
    if gender=='Male':
        gender=0
    else:
        gender=1

    name.append([gender])

#print(data)
# print(img_files[0])
# print(label[2])

data=np.array(data,dtype='float')/255.0     #Normalization of list/images
name=np.array(name)    #output label

(X_train,X_test,Y_train,Y_test)=train_test_split(data,name,test_size=0.2,random_state=42)
size=len(X_train)
Y_train=to_categorical(Y_train,num_classes=2)
Y_test=to_categorical(Y_test,num_classes=2)

augmented=ImageDataGenerator(rotation_range=25,height_shift_range=0.1,shear_range=0.2,width_shift_range=0.1,zoom_range=0.2,horizontal_flip=True)

inp_shape=(img_dims[1],img_dims[0],img_dims[2])
model=Sequential()

channel_Dimension=-1
if backend.image_data_format()=='channel_first':
    inp_shape=(img_dims[2],img_dims[1],img_dims[0])
    channel_Dimension=1
    
model.add(Conv2D(32,(3,3),padding='same',input_shape=inp_shape))
model.add(Activation('relu'))
model.add(BatchNormalization(axis=channel_Dimension))
model.add(MaxPooling2D(pool_size=(3,3)))
model.add(Dropout(0.25))
    
model.add(Conv2D(64,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(BatchNormalization(axis=channel_Dimension))

model.add(Conv2D(64,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(BatchNormalization(axis=channel_Dimension))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))


model.add(Conv2D(128,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(BatchNormalization(axis=channel_Dimension))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(2))   
model.add(Activation('sigmoid'))


adam1=Adam(lr=0.001,decay=0.001/50)
model.compile(loss='binary_crossentropy',optimizer=adam1,metrics=['accuracy'])

fit_model=model.fit_generator(augmented.flow(X_train,Y_train,batch_size=64),validation_data=(X_test,Y_test),steps_per_epoch=size//64,epochs=50,verbose=1)
model.save('GenderClassifier.model')


