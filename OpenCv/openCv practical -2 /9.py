# Extracting object from the image and place on another image
# Random fingure ROI Background subtraction.
# load two images
import cv2
import numpy as np

img1 = cv2.imread("images/hero1.jpg")
img2 = cv2.imread("images/strom_breaker.JPG")

img1 = cv2.resize(img1, (1024,650))
img2 = cv2.resize(img2, (600,650))
# I want to fix image 2 data into img1

r,c,ch = img2.shape
# roi
roi = img1[0:r, 0:c]
# Now creating mask from img2
img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# create mask using threshold for objects detect

_, mask = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
# removing objects
mask_inv = cv2.bitwise_not(mask)
# put mask into roi
img2_bg = cv2.bitwise_and(roi, roi, mask=mask)


# Take only region of figure from original image
img2_fg = cv2.bitwise_and(img2, img2,mask=mask)



# cv2.imshow("Thor", img1)
# cv2.imshow("Strom Breaker", img_gray)
# cv2.imshow("roi", roi)
cv2.imshow("step -1", img_gray)
cv2.imshow("step -2", mask)
cv2.imshow("step -3", mask_inv)
cv2.imshow("step -4", img2_bg)
cv2.imshow("step -5", img2_fg)

cv2.waitKey(0)
cv2.destroyAllWindows()

