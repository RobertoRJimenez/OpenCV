import cv2
import numpy as np

def click_event(event, x, y, flags, param):

    # Checks if the left mouse click occurred
    if event == cv2.EVENT_LBUTTONDOWN:
        # puts the (x,y) of the click on the image
        print(x, ', ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX

        strXY = str(x) + ', ' + str(y)

        cv2.putText(img, strXY, (x,y), font, 1, (255,255,0), 2)

        cv2.imshow('image', img)
    # Checks if the right mouse button is clicked
    if event == cv2.EVENT_RBUTTONDOWN:

        # Gets the BGR of the pixel clicked on

        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)

        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)

        cv2.imshow('image', img)


#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('watch.jpg')
cv2.imshow('image', img)
# Keeps going till a key press
cv2.setMouseCallback('image', click_event)
# waits for key press
cv2.waitKey(0)

cv2.destroyAllWindows()