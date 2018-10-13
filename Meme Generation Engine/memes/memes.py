import numpy as np 
import os
import cv2

import random
a= random.randint(1,20)
print(a)

a2=str(a) + ".jpg"

img = cv2.imread(a2, 1)
resized_image = cv2.resize(img, (500, 500))

cv2.imshow('img',resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()