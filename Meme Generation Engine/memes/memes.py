import numpy as np 
import os
import cv2

import random
a= random.randint(1,21)
print(a)

a2=str(a) + ".jpg"

img = cv2.imread(a2, 1)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()