"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: Face detection
Found initialization on Kaggle
"""

import cv2 as cv
import argparse


class FaceDetection2:
    def __init__(self, object_cascade_path):
        """
        Initalize face detection
        :param object_cascade_path:
        """
        self.objectCascade = cv.CascadeClassifier(object_cascade_path)
def detectDisplay
    frame_grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_grey = cv.equalizeHist(frame_grey)
    faces = face_cascade.detectMultiScslr(frame_grey)

    for(x,y,w,h) in faces:
        center = (x+w//2,y+h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0,255),4)

        faceROI = frame_grey[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(faceROI)
        for (x2, y2,w2,h2) in eyes:
            eye_center = (x +x2 +w2//2, y+y2+h2//2)
            radius = int(round((w2+h2)*.25))
            frame = cv.circle(frame, eye_center, radius, (255,0,0),4)