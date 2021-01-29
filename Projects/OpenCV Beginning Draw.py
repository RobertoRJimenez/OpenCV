import cv2
import numpy as np

# Get image
# img = cv2.imread('watch.jpg', 1)

# Set img by using numpy's array
img = np.zeros([512,512,3], np.uint8)

# Sets the line
img = cv2.line(img, (0,0), (255,255),(0,0,255),5)

# Sets arrow line
img = cv2.arrowedLine(img, (0,255), (255,255),(255,0,0), 10)

# Sets Rectangle
img = cv2.rectangle(img, (384,0),(510,128), (0,0,255),10)

# Sets Circle
img = cv2.circle(img, (447,63), 63, (0,255,0),-1)

# Writes words to img
# Set Font
font = cv2.FONT_HERSHEY_SIMPLEX
img =cv2.putText(img, "OpenCv",(10,500), font, 4,(0,255,255), 10, cv2.LINE_AA)

# Show iamge
cv2.imshow('image', img)

# wait for key press and take the value
cv2.waitKey(0)
cv2.destroyAllWindows()
