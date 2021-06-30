# Morphological transformations are normally performed on binary images
import  cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)
# kernal = np.ones((2,2) , np.uint8)
kernal = np.ones((3,3) , np.uint8)
print(kernal)
dilation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing  = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)


title = ['image', 'mask', 'dialation', 'erosion', 'opening', 'closing']
images = [img, mask, dilation, erosion, opening, closing]

for i in range(len(title)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()