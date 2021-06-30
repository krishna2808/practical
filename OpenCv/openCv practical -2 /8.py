# (2) Adapative Thresholding in this no data lose of image that is means multiple threshoding it isn't same for simaple Thresholding

import cv2
import numpy as np
img = cv2.imread("images/sudoku.png", 0)
img = cv2.resize(img, (400,400))
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Image", img)
cv2.imshow("Adaptive Threshold", th)
cv2.waitKey(0)
cv2.destroyAllWindows()