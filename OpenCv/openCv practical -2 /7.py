# Thresholding
# (1) simple threading (2) Adapative Thresholding
import cv2
import numpy as np
img = cv2.imread('images/sudoku.png', 0)


_,threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_,threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
_,threshold = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)
_,threshold = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO)
_,threshold = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("threshold", threshold)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
