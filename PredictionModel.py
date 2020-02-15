"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: The purpose of this class is to make predictions
    based on the trained model
"""

import keras
import keras.models


class PredictionModel:
    def __init__(self):
        """
        Initialize the prediction model
        """
        self.model_path = 'saved_model_240_8_32_0.05_1_0.0001_100_156_2_True_True_fitted_objects.h5'

    def predict(self, frame):
        """
        Make predictions based on the image/video sent as a parameter
        :param frame: image/video sent in to be analyzed
        :return: Return if the frame has been edited visually or through audio
        """
        model = keras.models.load_model(self.model_path)

        predicted = model.predict(frame)

        labels = ['fake', 'real']

        i = predicted.argmax(axis=0)[0]

        return labels[i]  # predict true always until the model is up and running