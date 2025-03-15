import pickle

import cv2
import numpy as np
import face_recognition as fr
from pathlib import Path

path = "Picture/Me"
encoding_location = "Picture/encodeMe/encode.pkl"
names = []
encodings = []

for filepath in Path(path).glob("*"):
    name = "ME"
    print(filepath)
    img = cv2.imread(f"{filepath}", 1)
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("ME", img)
    cv2.waitKey(0)

    faceLocation = fr.face_locations(img, model="cnn")
    faceEncoding = fr.face_encodings(img, faceLocation)
    for encoding in faceEncoding:
        names.append(name)
        encodings.append(encoding)

    name_encodings = {"name": names, "encoding": encodings}
    with  .open(mode="wb") as f:
        pickle.dump(name_encodings, f)
