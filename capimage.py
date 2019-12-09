import cv2
import os
import time
import numpy as np
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
path='images/'
dim=(640,480)
name=input('Tên: ')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
img_num = 200

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)

while True:
    ret, frame = cam.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 1)
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)
    for (x, y, w, h) in faces:
        resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite((path + (str(name) + str(img_counter)) + '.png'), frame)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 255, 255), 1)
        img_counter += 1
    cv2.putText(frame, "Process: "+str(int(img_counter/img_num*100))+ "%".title(), (10, 45), font, 1, (255, 255, 255), 1)
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if ((k%256 == 27) | (img_counter == img_num)):
        print("__GETTING IMAGES SUCCESSFULLY__")
        break
cam.release()

cv2.destroyAllWindows()
