
import cv2
import numpy as np
#doc anh
img = cv2.imread("Picture/anh 1.jpg", 1)
#resize anh
#img = cv2.resize(img, (1920, 1200))
#xuat anh theo ti le anh ban dau
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
#xoay anh
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#xuat anh
cv2.imshow("anh", img)
#thoi gian xem anh theo mili giay
cv2.waitKey(3000)
#luu anh
#cv2.imwrite("Picture/anh 1 copy.jpg", img)
