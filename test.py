from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
import shutil
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
import pkg_resources
from mtcnn.exceptions import InvalidImage
from mtcnn.network.factory import NetworkFactory
import pandas as pd
import serial
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)


video=cv2.VideoCapture(0)
detector = MTCNN()



while True:
    ret,frame=video.read()
    faces = detector.detect_faces(frame)
    total_count = len(faces)
    
        
    for result in faces:
        x,y,w,h = result['box']
        crop_img=frame[y:y+h, x:x+w, :]
        face_roi = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        if(total_count>1):
            fdata="Detected"
        else:
            fdata="No"
        arduino.write(str(fdata).encode('utf-8'))
        cv2.putText(frame, f'Count: {total_count}', 
                        (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        time.sleep(1)
        arduino.flushInput()
    cv2.imshow('Recognition', frame)
    k=cv2.waitKey(1)
    if k==ord('o'):
        
        time.sleep(5)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()

