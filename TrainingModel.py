"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: This is the code for training the neural network
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import os

# Initialize the training model
directory = os.getcwd()
index = directory.index("DeepFakeDetection")
slash = "/"
if os.name == 'nt':
    slash = "\\"
directory = directory[0:index] + 'DeepFakeData' + slash
train_file = directory + 'train_sample_videos'

print("The training data is: ", train_file)

df = pd.read_json(os.path.join(train_file, 'metadata.json'))
meta_train_df = df.T

meta_train_df.head()

