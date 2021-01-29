import matplotlib.pylab as plt
import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#img = cv2.imread('face.jpg')

cap = cv2.VideoCapture('face.mp4')

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    count = 0
    eye = 0
    for (x, y, w, h) in faces:
        count = count + 1
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
        cv2.putText(img, "face " + str(count), (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_color)
        for(ex, ey, ew, eh) in eyes:
            eye = eye + 1
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
            cv2.putText(roi_color, "eye " + str(eye), (ex, ey), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()