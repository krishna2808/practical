# Bitwise operation for images.

import cv2
import numpy as nm
import numpy as np

img1 = np.zeros((250,250,3), np.uint8)
img2 = np.zeros((250,250,3), np.uint8)
img1 = cv2.rectangle(img1, (100, 0), (200, 100), (255, 255, 255), -1)
img2 = cv2.rectangle(img2, (100, 0), (200, 100), (255, 255, 255), 1 )
cv2.imshow('image 1', img1)
cv2.imshow('image 2', img2)
bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)

cv2.imshow('bitAnd', bitAnd )
cv2.imshow('bitOr ', bitOr )
cv2.imshow('image Xor', bitXor)
cv2.imshow('image 1  Not', bitNot1)

cv2.waitKey(0)
cv2.destroyAllWindows()