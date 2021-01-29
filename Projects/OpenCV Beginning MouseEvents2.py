import cv2
import numpy as np

def click_event(event, x, y, flags, param):

    # Checks if the left mouse click occurred
    if event == cv2.EVENT_LBUTTONDOWN:
        # First click leaves red dot/circle
        # then afterwards will leave another red dot/circle
        # but will be connected by blue dash
        cv2.circle(img, (x,y), 3, (0,0,255),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,0,0),5)
        cv2.imshow('image',img)





img = np.zeros((512,512,3), np.uint8)
#img = cv2.imread('watch.jpg')
cv2.imshow('image', img)
points = []
# Keeps going till a key press
cv2.setMouseCallback('image', click_event)
# waits for key press
cv2.waitKey(0)

cv2.destroyAllWindows()