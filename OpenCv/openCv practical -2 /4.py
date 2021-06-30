import cv2
import numpy as np
img1 = cv2.imread("images/smarties.png")
img2 = cv2.imread("images/messi5.jpg")
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

def krishan(x):
    pass

img3 = np.zeros((400, 400, 3), np.uint8)
cv2.namedWindow("win")
switch = '0 : OFF\n1 :ON'
cv2.createTrackbar(switch, 'win', 0,1, krishan)
cv2.createTrackbar('Alpha','win', 1,100, krishan)
while True:
    s = cv2.getTrackbarPos(switch, 'win')
    a = cv2.getTrackbarPos('Alpha', 'win')
    n = float(a/100)
    if s ==0 :
        dst = img3[:]
    else:
        dst = cv2.addWeighted(img1,1-n, img2, n, 0)
        cv2.putText(dst, str(a), (20,50), cv2.FONT_ITALIC, 2, (0, 125, 255), 2)
    cv2.imshow('dst', dst)
    if  cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
