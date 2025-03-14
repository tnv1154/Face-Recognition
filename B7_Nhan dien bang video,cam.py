
import cv2
import face_recognition
import numpy as np
import face_recognition as fr
import os #load thư viện ảnh

path = "Picture/pic2"
#lưu ma trận điểm ảnh
imges = []
#lưu tên các file ảnh
classNames = []
#load tên toàn bộ ảnh + đuôi trong thư mục vào list
myList = os.listdir(path)
for name in myList:
    #đọc ảnh có đường dẫn path/tên file
    currentImg = cv2.imread(f"{path}/{name}")
    #lưu ma trận ảnh từng ảnh vào list
    imges.append(currentImg)
    #Tách tên file của ảnh thành 2 phần đường dẫn + tên và đuôi
    #os.path.splitext(name)[1] tách lấy đuôi file
    classNames.append(os.path.splitext(name)[0]) #lấy tên ảnh

def maHoa(images):
    """Mã hóa list ảnh"""
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeList.append(fr.face_encodings(img))
    return encodeList

encodeList = maHoa(imges)
print("Ma hoa thanh cong")
print(len(encodeList))

#Mở cam
cap = cv2.VideoCapture(0)
