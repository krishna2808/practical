# HSV (hua saturation value)
# detect color in an videocamp

import cv2
import numpy as np
# frame = cv2.imread('images/smarties.png')
cap = cv2.VideoCapture(1)
# frame = cv2.resize(frame, (600, 400))
def krishna(x):
     pass
cv2.namedWindow("color Adjustment")

cv2.createTrackbar("Lower H", "color Adjustment", 0, 255, krishna)
cv2.createTrackbar('Lower S', "color Adjustment", 0, 255, krishna)
cv2.createTrackbar('Lower V', "color Adjustment", 0, 255, krishna)

cv2.createTrackbar('Upper H', "color Adjustment", 255, 255, krishna)
cv2.createTrackbar('Upper S', "color Adjustment", 255, 255, krishna)
cv2.createTrackbar('Upper V', "color Adjustment", 255, 255, krishna)

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.resize(frame, (400, 400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower H", "color Adjustment")
    l_s = cv2.getTrackbarPos("Lower S", "color Adjustment")
    l_v = cv2.getTrackbarPos("Lower V", "color Adjustment")

    u_h = cv2.getTrackbarPos("Upper H", "color Adjustment")
    u_s = cv2.getTrackbarPos("Upper S", "color Adjustment")
    u_v = cv2.getTrackbarPos("Upper V", "color Adjustment")

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h,u_s, u_v])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    # filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original ", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()