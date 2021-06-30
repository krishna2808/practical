import cv2
import numpy as np

cap = cv2.VideoCapture('videos/vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # ret, frame = cap.read()


    if cv2.waitKey(40) ==27:
        break
cap.release()
cv2.destroyAllWindows()
