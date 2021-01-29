import cv2

# Get image
img = cv2.imread('watch.jpg', 1)

print(img)

# Show iamge
cv2.imshow('image', img)

# wait for key press and take the value
k = cv2.waitKey(0)
# Press the esc key
if k == 27:

    cv2.destroyAllWindows()
# press the s button
elif k == ord('s'):

    cv2.imwrite('copy of watch.jpg',img)
    cv2.destroyAllWindows()
