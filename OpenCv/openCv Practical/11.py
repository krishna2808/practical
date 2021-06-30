# Canny edge detection
# The canny edge detection algorithms is composed of 5 steps
# 1 Noise reducing
# 2 Gradient calculation
# 3 Non-maximum suppression
# 4 Double Threshould
# 5 Edge Tracking by Hysteresis
import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.png')

canny = cv2. Canny(img, 100, 200)

tiltes = ['Image', 'Canny']
images = [img, canny]
for i in range(len(images)):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(tiltes[i])
    plt.xticks([]), plt.yticks([])

plt.show()