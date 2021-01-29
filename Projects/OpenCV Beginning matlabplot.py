import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('fieldman.jpg', -1)
cv2.imshow("img", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

# wait for key press and take the value
cv2.waitKey(0)
cv2.destroyAllWindows()
