"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: Face detection
Found initialization on Kaggle
"""

import cv2 as cv


class FaceDetection:
    def __init__(self, object_cascade_path):
        """
        Initalize face detection
        :param object_cascade_path:
        """
        self.objectCascade = cv.CascadeClassifier(object_cascade_path)

    def detect(self, image, scale_factor=1.3, min_neighbor=5, min_size=(20, 20)):
        """
        Detect the object in the image
        :param image: frame
        :param scale_factor: scale the frame
        :param min_neighbor: minimum number of parameters considered during object detection
        :param min_size: minimum image size
        :return: return the detection
        """
        rects = self.objectCascade.detectMultiScale(image,
                                                    scaleFactor=scale_factor,
                                                    minNeighbors=min_neighbor,
                                                    minSize=min_size)
        return rects
