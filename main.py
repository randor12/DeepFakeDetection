"""
:author: Ryan Nicholas
:date: February 15, 2020
:description: Test out the prediction model
"""

import PredictionModel as pm

get_audio = 'realtalk/real/JRE1169-0025.wav'


prediction = pm.PredictionModel()

print(prediction.predict(get_audio))
