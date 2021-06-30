# Image Analyzation uisng Histogram
import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
img = np.zeros((200, 200), np.uint8)
cv2.rectangle(img, (0,100), (200,200),(255),-1)
cv2.rectangle(img, (0,50),(50,100),(127),-1)

hist = cv2.calcHist([img], [0], None, [256],[0,256])


plt.plot(hist)
plt.show()
cv2.imshow("res", img)
cv2.imshow("Hist", hist)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# with color image
""""
img = cv2.imread("images/hero1.jpg")
img = cv2.resize(img, (500,650))
b,g,r = cv2.split(img)
cv2.imshow("image", img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.title("colorfull Image")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Gray scale images
""""
img = cv2.imread("images/hero1.jpg")
img = cv2.resize(img, (500,650))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist(img_gray, [0],None, [256], [0,256])
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
 """
# Histogram equaliztion is good when of the image is confined to a particular region
# it accept gray scale image
img = cv2.imread("images/hero1.jpg")
img = cv2.resize(img, (500,650))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equl = cv2.equalizeHist(img_gray)
res = np.hstack((img_gray,equl))
cv2.imshow("equl", res)
hist1 = cv2.calcHist([equl], [0], None, [256], [0,256])
plt.plot(hist1)
plt.title("Equalization")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()