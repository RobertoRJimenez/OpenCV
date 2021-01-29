import cv2
import numpy as np

def click_event(event, x, y, flags, param):

    # Checks if the left mouse click occurred
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x, 0]
        green = img[y,x, 1]
        red = img[y,x, 2]

        cv2.circle(img, (x,y), 3, (0,0,255),-1)

        mycolorImage = np.zeros((512,512,3), np.uint8)

        mycolorImage[:] = [blue, green, red]

        cv2.imshow('color', mycolorImage)



#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('watch.jpg')
cv2.imshow('image', img)
points = []
# Keeps going till a key press
cv2.setMouseCallback('image', click_event)
# waits for key press
cv2.waitKey(0)

cv2.destroyAllWindows()