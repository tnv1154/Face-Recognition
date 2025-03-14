

import cv2
import face_recognition


"""Xác định vị trí khuôn mặt"""
#đọc ảnh
imgElon = face_recognition.load_image_file("Picture/elon musk.jpg")
#Chuyển tử ảnh BGR sang RGB
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgCheck = face_recognition.load_image_file("Picture/elon check.jpg")
imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)

#Xác định vị trí khuôn mặt
faceLoc = face_recognition.face_locations(imgElon)
#faceLoc là mảng 2 chiều
#Tạo độ khuôn mặt (y1, x2, y2, x1)
print(faceLoc)

#Mã hóa hình ảnh
encodeElon = face_recognition.face_encodings(imgElon)
#Vẽ hình vuông theo tọa độ khuôn mặt (x1, y1, x2, y2)
cv2.rectangle(imgElon, (faceLoc[0][3], faceLoc[0][0]), (faceLoc[0][1], faceLoc[0][2]), (255, 0, 0), 2)

faceCheck = face_recognition.face_locations(imgCheck)
encodeCheck = face_recognition.face_encodings(imgCheck)
cv2.rectangle(imgCheck, (faceCheck[0][3], faceCheck[0][0]), (faceCheck[0][1], faceCheck[0][2]), (255, 0, 0), 2)



#So sánh khuôn mặt qua encode
result = face_recognition.compare_faces([encodeElon[0]], encodeCheck[0])
print(result)

#Sai số giữa các bức ảnh càng nhỏ thì càng giống
faceDis = face_recognition.face_distance([encodeElon[0]], encodeCheck[0])
print(faceDis)

cv2.putText(imgCheck, f"{str(result)}{(1 - round(faceDis[0],2)) * 100}%", (faceLoc[0][3], faceLoc[0][0] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.imshow("", imgCheck)
cv2.imshow("Elon", imgElon)
cv2.waitKey()