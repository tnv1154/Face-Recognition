
import cv2
import numpy as np
import face_recognition as fr
from pathlib import Path

pathMe = Path("Picture/Me")
encodes = []

for filepath in pathMe.glob("*.jpg"):
    name = "ME"
    img = cv2.imread(filepath)
    img = cv2.resize(img, (0, 0), fx=1, fy=1)
    faceLoc = fr.face_locations(img)
    encodeFace = fr.face_encodings(img, faceLoc)
    encodes.append(encodeFace)

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    faceLoc = fr.face_locations(frame)
    encodeCurr = fr.face_encodings(frame, faceLoc)

    for faceLocCurr, encodeCurrFace in zip(faceLoc, encodeCurr):
        match = fr.compare_faces(encodes, encodeCurrFace)
        dis = fr.face_distance(encodes, encodeCurrFace)
        #vị trí dis nhỏ nhất
        matchIdx = np.argmin(dis)
        if dis.any() < 0.5:
            name = "ME"
        else:
            name = "UNKNOWN"
        y2, x1, y1, x2 = faceLocCurr
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        frame = cv2.putText(frame, f"{name}", (x1 + 5, y1 + 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()