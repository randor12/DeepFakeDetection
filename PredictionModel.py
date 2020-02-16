"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: The purpose of this class is to make predictions
    based on the trained model
"""

import numpy as np
from ExtractionScript import *
import pickle


class PredictionModel:
    def __init__(self):
        """
        Initialize the prediction model
        """
        self.model_path = 'models/MyModel.sav'

    def predict(self, frame):
        """
        Make predictions based on the image/video sent as a parameter
        :param frame: image/video sent in to be analyzed
        :return: Return if the frame has been edited visually or through audio
        """
        model = pickle.load(open(self.model_path, 'rb'))

        process = np.max(extract_features(frame)).reshape((1, 1))

        predicted = model.predict(process)

        labels = ['FAKE', 'REAL']

        print("Prediction: ", labels[predicted[0]])
        return labels[predicted[0]]

