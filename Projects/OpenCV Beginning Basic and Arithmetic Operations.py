import cv2
import numpy as np

img = cv2.imread('fieldman.jpg')

img2 = cv2.imread('flower.jpg')
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#Get the mans head to end of Torso
Manbody = img[56:151, 71:121]

#Place the copied pixels to next to man
img[56:151, 10:60] = Manbody

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2);
dst = cv2.addWeighted(img, .9, img2, .1, 0)

cv2.imshow("img1", dst)

# wait for key press and take the value
cv2.waitKey(0)
cv2.destroyAllWindows()
