#ROI  (Region of interest)
import cv2
import numpy as np

img = cv2.imread("images/messi5.jpg")

# image axis --> (x1, y1)--> (332,287), (x2, y2) --> (395, 335)
# img[(y1, y2), (x1, x2)]
ball = img[287:337, 332:395]

# x2-x1 = 332 - 395 = 63 --->
# y2- y1 = 337 - 287 = 50
resX = 395 - 332
img[287:337 , 65:65+resX] = ball
resY = 80 - 30
img[30:30+resY ,332:395] = ball

cv2.imshow("image", img)
cv2.imshow("ball", ball)
cv2.waitKey(0)
cv2.destroyAllWindows()