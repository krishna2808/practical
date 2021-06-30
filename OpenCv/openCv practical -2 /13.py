# face adn Eye detection
# face detection using haasrcascade file
import cv2
import numpy as np

image = cv2.imread("images/krishna.jpeg")
image = cv2.resize(image, (800,600))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# parameters (img, scale, factor[reduce image size], min, neighbour)
face = cv2.CascadeClassifier("xml/face.xml")
eye = cv2.CascadeClassifier("xml/eye.xml")
faces = face.detectMultiScale(gray, 1.2,2)
for (x,y,w,h) in faces:
    image = cv2.rectangle(image, (x,y), (x+w, y+h), (127, 0, 205), 3)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(roi_gray, 1.2, 1)
    for (ex, ey, ew,eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255,0,0),2)




cv2.imshow("original ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

