"""
:author: Ryan Nicholas, Matt Gonley
:date: 2/15/2020
:description: Newer Training Model
"""

from pandas import DataFrame
from sklearn.linear_model import LinearRegression
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
        self.data.append(self.dataFrameFromDirectory(os.path.join(train_file, 'fake'), 'FAKE'))
        self.data.append(self.dataFrameFromDirectory(os.path.join(train_file, 'real'), 'REAL'))
        counts = self.data['audio'].values
        targets = self.data['label'].values
        classifier = LinearRegression()
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
        row = []
        index = []

        for filename, value in self.readFiles(path):
            row.append({"audio": value, "label": classification})
            index.append(filename)

        return DataFrame(row, index=index)

    def readFiles(self, path):
        """
        Read the files from a directory
        :param path: path for the files
        :return: values
        """
        for root, dirnames, files in os.walk(path):
            file = os.path.join(path, files)
            val = extract_features(file)
            yield file, val
