"""
:author: Ryan Nicholas, Matt Gonley
:date: 2/15/2020
:description: Newer Training Model
"""

from pandas import DataFrame
import keras
from keras.models import Sequential
from sklearn import preprocessing
from keras.layers import *
from ExtractionScript import *
import pickle


class Train():
    def __init__(self):
        """
        Initialize the Training class
        """
        self.data = DataFrame({'audio': [], 'label': []})
        direct = os.getcwd()
        train_file = os.path.join(direct, 'realtalk')
        self.data = self.data.append(self.dataFrameFromDirectory(os.path.join(train_file, 'fake'), 'FAKE'))
        self.data = self.data.append(self.dataFrameFromDirectory(os.path.join(train_file, 'real'), 'REAL'))
        counts = self.data['audio'].values
        targets = preprocessing.LabelEncoder().fit_transform(self.data['label'].values)

        print(targets.shape)

        counts = counts.reshape((24, 1, 1))

        print(counts.shape)

        # Construct model
        classifier = Sequential()
        classifier.add(
            Conv1D(filters=16, kernel_size=2, input_shape=(1, 1), activation='relu', padding='same'))
        classifier.add(MaxPooling1D(pool_size=2, padding='same'))
        classifier.add(Dropout(0.2))

        classifier.add(Conv1D(filters=32, kernel_size=2, activation='relu', padding='same'))
        classifier.add(MaxPooling1D(pool_size=2, padding='same'))
        classifier.add(Dropout(0.2))

        classifier.add(Conv1D(filters=64, kernel_size=2, activation='relu', padding='same'))
        classifier.add(MaxPooling1D(pool_size=2, padding='same'))
        classifier.add(Dropout(0.2))

        classifier.add(Conv1D(filters=128, kernel_size=2, activation='relu', padding='same'))
        classifier.add(MaxPooling1D(pool_size=2, padding='same'))
        classifier.add(Dropout(0.2))
        classifier.add(GlobalAveragePooling1D())

        classifier.add(Dense(1, activation='softmax'))

        classifier.compile(optimizer='adam',
                           loss='binary_crossentropy',
                           metrics=['accuracy'])
        classifier.build(input_shape=(24, 1))
        classifier.fit(counts, targets)
        model_file = 'models/MyModel.pkl'
        with open(model_file, 'wb') as file:
            pickle.dump(classifier, file)



    def dataFrameFromDirectory(self, path, classification):
        """
        Append data frame
        :param path: directory path
        :param classification: classification
        :return: appended Dataframe
        """
        rows = []
        index = []

        for filename, value in self.readFiles(path):
            rows.append({'audio': np.mean(value), 'label': classification})
            index.append(filename)
        return DataFrame(rows, index=index)

    def readFiles(self, path):
        """
        Read the files from a directory
        :param path: path for the files
        :return: values
        """
        for root, dirnames, files in os.walk(path):
            for filename in files:
                file = os.path.join(root, filename)
                val = extract_features(file)
                yield file, val
