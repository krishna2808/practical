# Break video into multiple images and store folder

import cv2
def videoToImage():
    vidcap = cv2.VideoCapture('/home/krishna/Desktop/demo.mp4')
    ret, image = vidcap.read()
    count = 0
    while vidcap.isOpened():
        if ret:
            cv2.imshow("vidoe to image", image)
            cv2.imwrite("/home/krishna/Desktop/folder/img-%d.jpg"%count, image)
            ret, image = vidcap.read()
            count += 1

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    vidcap.release()
    cv2.destroyAllWindows()
def imageToVideo():
    count = 0
    while True:
        try:
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            img = cv2.imread("/home/krishna/Desktop/folder/img-%d.jpg"%count)
            img = cv2.resize(img,(400,400))
            count += 1
            cv2.imshow("Image To Video", img)
        except :
            pass
videoToImage()
imageToVideo()
cv2.destroyAllWindows()