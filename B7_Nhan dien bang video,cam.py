
import cv2
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
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeList = maHoa(imges)
print("Ma hoa thanh cong")
print(len(encodeList))

#Mở cam
cap = cv2.VideoCapture("Picture/video-test.mp4")
while True:
    ret, frame = cap.read()
    framS = cv2.resize(frame, (0, 0), None ,fx=0.25, fy=0.25)
    framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)
    #Xác định vị trí khuôn mặt trên cam và encode
    faceCurrFrame = fr.face_locations(framS) #lấy vị trí từng khuôn mặt
    encodeCurFrame = fr.face_encodings(framS)
    #zip : chạy song song 2 list trong zip
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurrFrame):
        matches = fr.compare_faces([encodeList], encodeFace)
        faceDis = fr.face_distance([encodeList], encodeFace)
        cv2.rectangle(framS, (faceLoc[3],faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 2)
        if matches == True:
            cv2.putText(framS, f"{matches}{1-round(faceDis, 2)}", (faceLoc[0][3], faceLoc[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        print(faceDis)

    cv2.imshow("", framS)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()