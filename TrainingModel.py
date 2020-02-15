"""
:author: Ryan Nicholas, Matt Gonley
:date: February 14, 2020
:description: This is the code for training the neural network
"""
import datetime
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
import os
from ExtractionScript import create_DataFrame

#Extracion script does this.
featuresdf = create_DataFrame('./realtalk/')


#Converting data does this
from ConvertingData import ConvertData
x_train, x_test, y_train, y_test = ConvertData.splitData(featuresdf)


num_rows = 40
num_columns = 174
num_channels = 1

x_train = x_train.reshape(x_train.shape[0], num_rows, num_columns, num_channels)
x_test = x_test.reshape(x_test.shape[0], num_rows, num_columns, num_channels)

num_labels =ConvertData.yy.shape[1]
filter_size =2

#model
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=2, input_shape=(num_rows, num_columns, num_channels),
                 activation='relu'))

model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(.02))

model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=64, kernel_size=2, activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=128, kernel_size=2, activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))
model.add(GlobalAveragePooling2D())

model.add(Dense(num_labels, activation='softmax'))


#compile
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

model.summary()

score = model.evaluate(x_test, y_test, verbose=1)

accuracy = 100*score[1]

print("Pre-training accuracy: %.4f%%" % accuracy)

#training
num_epochs = 10 #may be changed
num_batch_size = 256 #may be changed


#do not know if this is right
checkerpointer = ModelCheckpoint(filepath='saved_Models/training.f5', verbose=1, save_best_only=True)

start = datetime.now()

model.fit(x_train, y_train, batch_size=num_batch_size, epochs=num_epochs,
          validation_data=(x_test, y_test), callbacks=[checkerpointer], verbose=1)
duration=datetime.now()-start

print("Traininng done in: ", duration)

#accuracy
score = model.evaluate(x_train, y_train, verbose=0)
print("Training accuracyL ", score[1])
score=model.evaluate(x_test, y_test, verbose=0)
print("training accuracy: ", score[1])


