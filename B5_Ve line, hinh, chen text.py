
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    #Vẽ line(nơi vẽ, vị trí bắt đầu, vị trí kết thúc, màu sắc, độ dày)
    #img = cv2.line(frame, (width // 2,0 ), (width, height), (0,0,0), 50)

    #Vẽ hình chữ nhật rectangle(nơi vẽ, vị trí bắt đầu, vị trí kết thúc, màu sắc, độ dày)
    #Độ dày bằng -1 thì phủ kín
    img = cv2.rectangle(frame, (width // 2, height // 2), (width, height), (0,0,0), -1)

    #Vẽ đường tròn circle
    img = cv2.circle(frame, (width // 2, height // 2), 70, (255,255,255), 5)

    #Chèn text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frame, "THANG", (550, 00), font, 3, (255,255,255), 3 )

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()