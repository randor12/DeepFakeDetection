"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: The purpose of this class is to make predictions
    based on the trained model
"""

import keras
import keras.models
import os
import numpy as np
import pickle
from ExtractionScript import *


class PredictionModel:
    def __init__(self):
        """
        Initialize the prediction model
        """
        self.model_path = 'models/MyModel.h5'

    def predict(self, frame):
        """
        Make predictions based on the image/video sent as a parameter
        :param frame: image/video sent in to be analyzed
        :return: Return if the frame has been edited visually or through audio
        """
        try:
            with open('models/MyModel.pkl', 'rb') as file:
                model = pickle.load(file)

            process = extract_features(frame)

            predicted = model.predict(process)

            labels = ['fake', 'real']

            i = predicted.argmax(axis=0)[0]

            return labels[i]
        except Exception:
            print("Model not found")
            return None