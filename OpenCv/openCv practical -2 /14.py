import cv2
import numpy as np


face = cv2.CascadeClassifier("xml/face.xml")
eye = cv2.CascadeClassifier("xml/eye.xml")

def dector(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3,5)
    for (x, y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (127,0,125), 3)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye.detectMultiScale(roi_gray, 1.2, 1)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex+27, ey+27), (ex + ew, ey + eh), (255, 0, 0), 2)

        # eyes = face.detectMultiScale2()
    return img
cap = cv2.VideoCapture(1)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 2)
    cv2.imshow("Face Detection", dector(frame))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()