# Smoothing Images ans Bluring images remove noise from images.
# in opencv some functions is available to Homogeneous filterm Gaussian filter, Median filter, Bilateral Filter.

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('images/lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernal)
blur = cv2.blur(img, (5, 5))
gb = cv2.GaussianBlur(img, (5, 5), 0)
medain = cv2.medianBlur(img, 5)
bilateralFilter= cv2.bilateralFilter(img, 9, 75, 75)

title = ['image', '2D Convolution','Blur', 'Gblur', 'Medain', 'Bilateralfiter']
images = [img, dst, blur, gb, medain, bilateralFilter]
for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()