# copy componets from images
import cv2
img = cv2.imread('images/messi5.jpg')
img2 = cv2.imread('images/opencv-logo.png')

print('Image Shape', img.shape)
print('image Size', img.size)
print('Image Datatype ', img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
# print(b)
# --------->   img[y1:y2, x1:x2]
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# cv2.imshow('image', r)
# cv2.imshow('image', ball)
# cv2.imshow('image', img)

# add two image
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .8, img2, .2, 0)
cv2.imshow('image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
