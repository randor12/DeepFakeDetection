"""
:author: Ryan Nicholas, Matt Gonley
:date: February 14, 2020
:description: This is the code for training the neural network
"""

from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from ExtractionScript import extract_features
import pandas as pd
import os


#Extracion script does this.
fulldatasetpath='./realtalk/'
metadata=pd.read_csv(fulldatasetpath+'metadata.json') # not quite sure what exactly is meant to be here
features=[]
for index, row in metadata.iterrows():
    file_name=os.path.join(os.path.abspath(fulldatasetpath),
                           'fold'+str(row['fold']+'/',str(row["slice_file_name"])))
    class_label = row["class_name"]
    data=extract_features(file_name)
    features.append([data, class_label])

featuresdf = pd.DataFrame(features, columns='[feature', 'class_label'])
print('Finished extracting from ', len(featuresdf), ' files')


#Converting data does this
X=np.array(featuresdf.feature.tolist())
y=np.array(featuresdf.class_label.tolist())

le = LabelEncoder()
yy=to_categorical(le.fit_transform(y))

x_train, x_test, y_train, y_test =
#train_test_split(X, yy, test_size=0.2, random_state=42)


num_rows = 40
num_columns = 174
num_channels = 1

x_train = x_train.reshape(x_train.shape[0], num_rows, num_columns, num_channels)
x_test = x_test.reshape(x_test.shape[0], num_rows, num_columns, num_channels)

num_labels =yy.shape[1]
filter_size =2


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

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

model.summary()

score = model.evaluate(x_test, y_test, verbose=1)

accuracy = 100*score[1]

print("Pre-training accuracy: %.4f%%" % accuracy)





num_epochs = 10 #may be changed
num_batch_size = 256 #may be changed

checkerpointer = ModelCheckpoint(filepath=''''filepath need to be stated''', verbose=1, save_best_only=True)

start = datetime.now()

model.fit(x_train, y_train, batch_size=num_batch_size, epochs=num_epochs,
          validation_data=(x_test, y_test), callbacks=[checkerpointer], verbose=1)
duration=datetime.now()-start

print("Traininng done in: ", duration)



score = model.evaluate(x_train, y_train, verbose=0)
print("Training accuracyL ", score[1])
score=model.evaluate(x_test, y_test, verbose=0)
print("training accuracy: ", score[1])


