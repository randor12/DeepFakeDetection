"""
:author: Ryan Nicholas, Matt Gonley
:date: 2/15/2020
:description: Newer Training Model
"""

from pandas import DataFrame
from sklearn.ensemble import *
from sklearn import preprocessing
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
        counts = counts.reshape(-1, 1)

        # Construct model
        """
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
        classifier.fit(counts, targets, epochs=10)
        model_file = 'models/MyModel.h5'
        classifier.save(model_file)
        """
        print(counts)
        print(targets)
        classifier = RandomForestClassifier()
        classifier.fit(counts, targets)

        model_save = 'models/MyModel.sav'
        pickle.dump(classifier, open(model_save, 'wb'))
        """
        val1 = np.max(extract_features('realtalk/real/JRE1169-0025.wav')).reshape((1, 1))
        print(val1)
        predict1 = classifier.predict(val1)
        #predict2 = classifier.predict('realtalk/fake/JREa633-0023.wav')
        word = 'REAL'
        if predict1[0] == 1:
            word = 'REAL'
        else:
            word = 'FAKE'
        print("Predict 1: ", word)
        #print("Predict 2: ", predict2)
        """



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
            rows.append({'audio': np.max(value), 'label': classification})
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
