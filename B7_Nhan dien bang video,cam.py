
import cv2
import numpy as np
import face_recognition as fr
import os #load thư viện ảnh

path = "Picture/pic2"
imges = []
classNames = []
#load tên toàn bộ ảnh trong thư mục vào list
myList = os.listdir(path)



print(myList)