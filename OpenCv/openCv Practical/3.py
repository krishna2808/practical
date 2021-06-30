# Events in openCv
import numpy as np
import cv2

def click_event(event, x,y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,' ', y)
        # strXY = str(x) + ', '+ str(y)
        # cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.circle(img, (x,y), 3, ( 0,0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (255, 0, 0) )
        cv2.imshow('image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        text = 'You are Right clicked '
        cv2.putText(img, text, (x, y), font, .5, (0,0, 255), 2)
        cv2.imshow('image', img)




img = np.zeros((512, 512,3), np.uint8)
points = []
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()