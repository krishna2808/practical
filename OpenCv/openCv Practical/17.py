# Image Contours
# it's used to heops in shape detection, Analyzation and recognition

import cv2
import numpy as np
# img = cv2.imread('images/opencv-logo.png')
img = cv2.imread('images/smarties.png')

img = cv2.resize(img, (400, 400))

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# ret, thresh = cv2.threshold(img1, 113, 255, 0, cv2.THRESH_BINARY_INV)
#
# # find contour
# cnst, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# # print(cnst, len(cnst))
# cont = cv2.drawContours(img, cnst, -1, (176, 10, 15, 15), 4)
# cv2.imshow('original ', img)
# cv2.imshow('Gray', img1)
# cv2.imshow('Thresh', thresh)
#
# cv2.imshow('Contours', cont)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()





def nothing(x):
    pass
cv2.namedWindow("Tracking")
cv2.createTrackbar('Set', 'Tracking', 0, 255, nothing)
while True:

    init = cv2.getTrackbarPos("Set", 'Tracking')
    print(init)

    ret, thresh = cv2.threshold(img1, init, 255,  cv2.THRESH_BINARY_INV)

    # find contour
    cnst, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    con = cv2.drawContours(img, cnst, -1, (176, 10, 15, 15), 4)


    # print(cnst, len(cnst))
    key = cv2.waitKeyEx(1)
    if key == 27:
        break
    cv2.imshow('original ', img)
    cv2.imshow('Gray', img1)
    cv2.imshow('Thresh', thresh)
    cv2.imshow('contours', con)

cv2.destroyAllWindows()