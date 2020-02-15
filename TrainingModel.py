"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: This is the code for training the neural network
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import os
import cv2 as cv
from skimage.transform import resize
import keras
from keras_preprocessing.image import ImageDataGenerator


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


train_labels = []

for t_label in meta_train_df.label:
    train_labels.append(t_label)

train_label_extra = []

# Get files
train_data = np.array(list(train_file + meta_train_df.index))
train_vids = []
count = 0
for x in train_data:
    cap = cv.VideoCapture(x)
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break
        train_vids.append(frame)
        train_label_extra.append(train_labels[count])
    count += 1
    cap.release()
    cv.destroyAllWindows()

storage = np.array([file for file in train_file if file.endswith('mp4')])

#print(train_data)
#print(storage.shape)

# videos are 432 x 288 size

x_train, x_test, y_train, y_test = train_test_split(train_vids, train_label_extra, test_size=0.2, random_state=42, train_size=0.8)

model = LinearRegression()
model.fit(train_vids, train_label_extra)
"""
accuracy_on_train = model.score(x_train, y_train)
accuracy_on_test = model.score(x_test, y_test)
print(accuracy_on_train, accuracy_on_test)

"""