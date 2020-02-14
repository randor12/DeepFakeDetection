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
import cv2 as cv
import FaceDetector as fd

def missing_data(data):
    """
    Display any missing data from the data set
    :param data: training data frame (df)
    :return: Missing data
    """
    total = data.isnull().sum()
    percent = (data.isnull().sum() / data.isnull().count()*100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtypes)
        types.append(dtype)
    tt['Types'] = types
    return np.transpose(tt)

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

# display the data frame of the training data
print(meta_train_df)

test_files = directory + 'test_videos'

