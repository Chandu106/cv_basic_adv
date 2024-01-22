import cv2 as cv
import numpy as np 
import os

people = []
haar_cascade = cv.CascadeClassifier("/home/chandu/cv_ws/haar_cascade_face.xml")

for i in os.listdir(r'/home/chandu/cv_ws/Resources/Faces/train'):
    people.append(i)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("/home/chandu/cv_ws/face_trained.yml")

img = cv.imread("/home/chandu/cv_ws/Resources/Faces/val/jerry_seinfeld/2.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, coonfidence = face_recognizer.predict(faces_roi)

    print('Label = {people[label]} with aconfidence of {coonfidence}')
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow("Detected Face", img)

cv.waitKey(0)

