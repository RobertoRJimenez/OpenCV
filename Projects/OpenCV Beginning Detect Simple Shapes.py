import cv2
import numpy as np
import math


img = cv2.imread('shapes.png')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thrash = cv2.threshold(imgGrey, 240 , 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 , 0))

    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        #print(aspectRatio)
        if aspectRatio >= .95 and aspectRatio <= 1.05:
            cv2.putText(img, 'Square', (x+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 , 0) )
        else:
            print(cv2.boundingRect(approx))
            cv2.putText(img, 'Rectangle', (x+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0) )

    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 , 0) )

    elif len(approx) == 10:
        cv2.putText(img, 'Star', (x+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 , 0) )

    else:
        cv2.putText(img, 'Circle', (x+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 , 0) )


cv2.imshow('image', img)
# wait for key press and take the value
cv2.waitKey(0)
cv2.destroyAllWindows()
