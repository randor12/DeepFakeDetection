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
from os import walk
import cv2 as cv
from skimage.transform import resize

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

test_file = directory + 'test_videos'

# Get all the names of the files in the training folder
f = []
for dirpath, dirnames, files in walk(train_file):
    f.extend(files)
    break

f.remove('metadata.json')

train_data = []

for vid in f:
    val = os.path.join(train_file, vid)
    cap = cv.VideoCapture(val)
    frameCount = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

    fc = 0
    ret = True
    videos = []
    while (fc < frameCount and ret):
        ret, buf[fc] = cap.read()

        videos.append(buf[fc])

        fc += 1

    train_data.append(videos)
    cap.release()

train_labels = []

for t_label in meta_train_df.label:
    train_labels.append(t_label)

x_train, x_test, y_train, y_test = train_test_split(train_data, train_labels, test_size=0.2, random_state=42)

model = SGDClassifier()
model.fit(x_train, y_train)

accuracy_on_train = model.score(x_train, y_train)
accuracy_on_test = model.score(x_test, y_test)
print(accuracy_on_train, accuracy_on_test)
