import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('fieldman.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0 , -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1].shape[1], gaussian_extended.shape[0])
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

