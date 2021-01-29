import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('flower.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)


cv2.imshow('Original image', img)
cv2.imshow('pyrDown 1 image', lr1)
cv2.imshow('pyrDown 2 image', lr2)
cv2.imshow('pyrUp 1 image', hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()

