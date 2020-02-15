"""

:author: Marcus Tran
:date: February 15th, 2020
:description: Functions to comb through a data set and then extract the features from audio files
in a given data path
Based on Medium Article and Example Code
"""

import pandas as pd
import os
import librosa
import numpy as np



def extract_features(fileName):

    try:
        audio, sample_rate = librosa.load(fileName, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T, axis=0)

    except Exception as error:
        print("Error encountered while parsing file: ", fileName)
        return None

    return mfccsscaled


def create_DataFrame(DataSetPath):

    # Set the path for the folder containing the dataset
    fulldatasetpath = DataSetPath

    metadata = pd.read_json(fulldatasetpath + 'metadata.json', orient='split')

    features = []
    # Extract features from each sound file
    for index, row in metadata.iterrows():

        fileName = os.path.join(os.path.abspath(fulldatasetpath),'fold'+
                                str(row["fold"])+'/',str(row["slice_file_name"]))

        class_label = row["class_name"]
        data = extract_features(fileName)

        features.append([data, class_label])

    # Converts the data into a data frame for use
    FeatureDataFrame = pd.DataFrame(features, columns=['feature', 'class_label'])

    print('Finished extracting from ', len(FeatureDataFrame), ' files')
    return FeatureDataFrame
