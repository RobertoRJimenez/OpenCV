import cv2
import numpy as np

# Set img by using numpy's array
img = np.zeros([512,512,3], np.uint8)
img2 = np.zeros([512,512,3], np.uint8)
# Sets Rectangle
img = cv2.rectangle(img, (200,0),(300,100), (255,255,255),-1)

img2 = cv2.rectangle(img2, (250,0),(512,512), (255,255,255),-1)

#bitAnd = cv2.bitwise_and(img2, img)
#bitOr = cv2.bitwise_or(img2, img)
#bitXor = cv2.bitwise_xor(img2, img)
bitNot1 = cv2.bitwise_not(img2)
bitNot2 = cv2.bitwise_not(img)

cv2.imshow("img1", img)
cv2.imshow("img2", img2)

#cv2.imshow('bitAnd', bitAnd)
#cv2.imshow('bitOr', bitOr)
#cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)


# wait for key press and take the value
cv2.waitKey(0)
cv2.destroyAllWindows()
