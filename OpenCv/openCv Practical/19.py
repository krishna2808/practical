# hand detection using contours
import cv2
import numpy as np
img = cv2.imread('images/hand.jpg')
img = cv2.resize(img, (400,400))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(img1, 9)
# dialation = cv2.dilate(blur, )
ret, threshold = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY_INV)
conts, hier = cv2.findContours(threshold, cv2.THRESH_BINARY_INV , cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, conts, -1, (50,50150,2), 2)
for c in conts:
   epsilon = 0.0001*cv2.arcLength(c, True)
   data = cv2.approxPolyDP(c, epsilon, True)
   hull = cv2.convexHull(data)
   cv2.drawContours(img, [c], -1, (50,50,150), 2)
   cv2.drawContours(img, [hull], -1, (0,255, 0), 2)

# find convexity defect
hull2 = cv2.convexHull(conts[0], returnPoints=False)
# defect returns an array which contain values
#
defect = cv2.convexityDefects(conts[0], hull2)
# for i in range(defect.shape[0]):
#     s,e,f,d = defect[i, 0]
#     start=tuple(c[s][0])
#     end=tuple(c[e][0])
#     far=tuple(c[f][0])
#     cv2.circle(img, far, 5, [0,0,255], -1)

c_max = max(conts, key=cv2.contourArea)
left_max = tuple(c_max[c_max[:, :, 0].argmin()][0])
right_max = tuple(c_max[c_max[:, :, 0].argmax()][0])
top_max = tuple(c_max[c_max[:, :, 1].argmin()][0])
down_max = tuple(c_max[c_max[:, :, 1].argmax()][0])

cv2.circle(img, left_max, 8, (255,0,255), -1)  # left
cv2.circle(img, right_max, 8, (0,125,255), -1)  # right
cv2.circle(img, top_max, 8, (255,10,0), -1)  # top
cv2.circle(img, down_max, 8, (19,0,255), -1)  # down

cv2.imshow("Origianl image", img)
cv2.imshow("Gray ", img1)
cv2.imshow("Threshold ", threshold)
cv2.waitKey(0)