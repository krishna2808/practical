# make Screen Recording
import cv2
import pyautogui as p
import numpy as np
# create Resolation
rs = p.size()
fn = input("Enter any file name and path : ->  ")

# for saving video make objects
fps = 30.0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(fn, fourcc, fps, rs)

# Create recording moduls
cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording", (600, 400))
while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live Recording", f)
    if cv2.waitKey(1) == ord('q'):
        break


output.release()
cv2.destroyAllWindows()
