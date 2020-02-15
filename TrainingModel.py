"""
:author: Ryan Nicholas, Matt Gonley
:date: February 14, 2020
:description: This is the code for training the neural network
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
from sklearn import metrics
import pandas as pd
import os
import librosa
from keras.callbacks import ModelCheckpoint
from datatime import datetime






num_rows = 40
num_columns = 174
num_channels = 1

x_train = x_train.reshape(x_train.shape[0], num_rows, num_columns, num_channels)
x_test = x_test.reshape(x_test.shape[0], num_rows, num_columns, num_channels)

num_labels =yy.shape[1]
filter_size =2









num_epochs = 10 #may be changed
num_batch_size = 256 #may be changed

checkerpointer = ModelCheckpoint(filepath=''''filepath need to be statedd''', verbose=1, save_best_only=True)

start = datetime.now()

model.fit(x_train, y_train, batch_size=num_batch_size, epochs=num_epochs,
          validation_data=(x_test, y_test), callbacks=[checkerpointer], verbose=1)
duration=datetime.now()-start

print("Traininng done in: ", duration)

