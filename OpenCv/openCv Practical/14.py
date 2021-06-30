import cv2
import numpy as np
img = cv2.imread('images/opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image', img)
cv2.imshow('Image Gray', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()


