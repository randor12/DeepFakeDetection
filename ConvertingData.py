"""
:author: Ryan Nicholas
:date: February 15, 2020
:description: Convert data to be ready for training
"""

from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import numpy as np
from pandas import DataFrame


class ConvertData():
    def __init__(self, vals):
        """
        Initialize Data
        :param df:
        """
        self.df = DataFrame(vals, columns=['index', 'label'])

    def splitData(self):
        """
        Split the data for the file
        :return:
        """
        # Get the x and y data
        x = np.array(self.df.index.tolist())
        y = np.array(self.df.label.tolist())

        # Encode the classification labels
        le = LabelEncoder()
        yy = to_categorical(le.fit_transform(y))

        # split the data
        from sklearn.model_selection import train_test_split

        x_train, x_test, y_train, y_test = train_test_split(x, yy, test_size=0.2, random_state=42, train_size=0.8)
        return (x_train, x_test, y_train, y_test)