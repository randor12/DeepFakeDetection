"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: The purpose of this class is to make predictions
    based on the trained model
"""


class PredictionModel:
    def __init__(self):
        """
        Initialize the prediction model
        """
        self.model_path = 'Model.h5'

    def predict(self, frame):
        """
        Make predictions based on the image/video sent as a parameter
        :param frame: image/video sent in to be analyzed
        :return: Return if the frame has been edited visually or through audio
        """
        prediction = True
        return prediction  # predict true always until the model is up and running