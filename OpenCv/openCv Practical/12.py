# Images Pyramids


import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.png')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)
layer = gp[-1]
# cv2.imshow('Uper level Gaussian Pyramid ', layer )
ip = [layer]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)


cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

