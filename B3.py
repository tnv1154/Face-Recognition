import random

import cv2
import numpy as np
#xu ly ma tran anh
img = cv2.imread("Picture/2.PNG", 1)

#print(img)
print(type(img))
print(img.shape)
print(img[0])

"""for i in range(200):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
cv2.imshow("anh", img)
cv2.waitKey()"""

vungChon = img[0:100, 500:700]
img[300:400,700:900] = vungChon
cv2.imshow("anh", img)
cv2.waitKey()