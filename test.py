import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
while True:
    ret, frame = cam.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (5,5), 1)
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 1)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 255, 255), 1)

    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break