
import cv2
import numpy as np
import face_recognition as fr
from pathlib import Path

path = "Picture/Me"
names = []
encodings = []

for filepath in path.glob("*"):
    name = "ME"
    print(filepath)
    img = cv2.imread(f"{path}/{filepath}", 1)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("ME", img)
    cv2.waitKey()

"""    faceLocation = fr.face_locations(img, model="cnn")
    faceEncoding = fr.face_encodings(img, faceLocation)

   for encoding in faceEncoding:
        names.append(name)
        encodings.append(encoding)"""

