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
