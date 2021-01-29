import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg")
_, w, h = template.shape[::-1]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
print(res)

threshold = .9
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv2.putText(img, "Messi", pt, cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cv2.imshow("img", img)

# wait for key press and take the value
cv2.waitKey(0)
cv2.destroyAllWindows()
