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

    cv.imshow('Capture', frame)

parser =argparse.ArgumentParser(description='Cascade code')
parser.add_argument('--face_cascade', help='Path tp face cascade', default='data/haarcascade_frontalface_alt.xml')
parser.add_argument('--eye', help='Path to eye cascade', default='data/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number', type=int, defualt=0)
args = parser.parse_args()

face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade

face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face image')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eye image')
    exit(0)
cam = args.camera
cap = cv.VideoCapture(cam)
if not cap.isOpened():
    print('--(!)Error opening cam')
    exit(0)
