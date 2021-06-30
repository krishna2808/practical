# Contour Moments and convexHull
import cv2
import numpy as np

img = cv2.imread('images/smarties.png')
img = cv2.resize(img, (400, 400))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img1, 190, 255, cv2.THRESH_BINARY_INV)
# find Contours
kernal = np.ones((3,3) , np.uint8)
print(kernal)
dilation = cv2.dilate(thresh, kernal, iterations=2)

cnts, hier = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cont = cv2.drawContours(img, cnts, -1, (176, 10, 15, 15), 4)

area1 = []
for c in cnts:
    M = cv2.moments(c)
    cX = int(M["m10"]/M['m00'])
    cY = int(M["m01"]/M["m00"])
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    # cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    # cv2.putText(img, 'center', (cX-20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # find area of contour
    area = cv2.contourArea(c)
    area1.append(area)
    epsilon = 0.01*cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, epsilon, True)
    hull = cv2.convexHull(data)
    x,y, w, h = cv2.boundingRect(hull)
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (125, 10,20, 0), 5)

print(area1)
# output ------------------
cv2.imshow('Original Image', img)
cv2.imshow('gray', img1)
cv2.imshow('Thresh', thresh)
# cv2.imshow('Contours', cont)

cv2.waitKey(0)
cv2.destroyAllWindows()