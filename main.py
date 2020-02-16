"""
:author: Ryan Nicholas
:date: February 15, 2020
:description: Test out the prediction model
"""

import Train

model = Train.Train()

from PredictionModel import PredictionModel

PredictionModel().predict('realtalk/real/JRE1169-0025.wav')
