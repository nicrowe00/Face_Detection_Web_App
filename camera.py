import cv2, os, face_recognition
import numpy as np

path = 'Faces'
images = []
classNames = []
myList = os.listdir(path)
for c1 in myList:
    curImg = cv2.imread(f'{path}/{c1}')
    images.append(curImg)
    classNames.append(os.path.splitext(c1)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images: 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def _del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame=self.video.read()
        imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurrentFrame = face_recognition.face_locations(imgS)
        encodesCurrentFrame = face_recognition.face_encodings(imgS,facesCurrentFrame)
        for encodeFace,faceLoc in zip(encodesCurrentFrame,facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
            matchIndex = np.argmin(faceDistance)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                faces=faceDetect.detectMultiScale(frame, 1.3, 5)
                for x,y,w,h in faces:
                    x1,y1=x+w, y+h
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
                    cv2.putText(frame, name,(x1+6,y1-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        ret, jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()

