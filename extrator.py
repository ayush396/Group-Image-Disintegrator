import cv2
import dlib
import shutil
import os

detector=dlib.get_frontal_face_detector()
new_path="env/extracted_pics/"
path="env/static/upload.jpg"
      

def save(img, name, bbox, width=180, height= 227):
    x, y, w, h = bbox
    imgCrop = img[y:h, x:w]
    imgCrop = cv2.resize(imgCrop, (width, height))
    cv2.imwrite(name+".jpg", imgCrop)  



class extract():
    def __init__(self) :
        pass
    
    def faces():
        frame = cv2.imread(path)
        frame2= cv2.imread(path)
    
        faces = detector(frame)
        fit = 20
        shutil.rmtree(new_path)
        os.makedirs(new_path)
        counter=0

        for face in faces:
            
            x, y = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x2, y2), (220,255,220), 1)

            w=x2-x
            h=y2-y
            cv2.line(frame, (x,y), (x+10, y), (0,250,0), 3)
            cv2.line(frame, (x,y), (x, y+10), (0,250,0), 3)

            cv2.line(frame, (x+w, y), (x+w-10, y), (0,250,0), 3)
            cv2.line(frame, (x+w, y), (x+w, y+10), (0,250,0), 3)

            cv2.line(frame, (x, y+h), (x, y+h-10), (0,250,0), 3)
            cv2.line(frame, (x, y+h), (x+10, y+h), (0,250,0), 3)
            cv2.line(frame, (x+w, y+h), (x+w, y+h-10), (0,250,0),3)
            cv2.line(frame, (x+w, y+h), (x+w-10, y+h), (0,250,0),3)

            save(frame2, new_path+str(counter), (x-fit, y-fit, x2+fit, y2+fit))
            counter=counter+1
            
        frame = cv2.resize(frame, (800,800))
        

