import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


trainning_data_normalized = np.load('C:/Users/bytes 2.0/Desktop/Projects/Self-Driving-NeuralNetwork/Trainning_Normalized_data.npy', allow_pickle=True)


train_set = trainning_data_normalized[:-2000]
testing_set = trainning_data_normalized[-2000:]

X = np.array([i[0] for i in train_set])
Y = np.array([i[1] for i in train_set])

X_test = np.array([i[0] for i in testing_set])
Y_test = np.array([i[1] for i in testing_set])


model = keras.models.Sequential()
model.add(layers.Conv2D(92,(3,3), activation = 'relu', input_shape=(150,200,1)))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Conv2D(92, (3,3), activation = 'relu',))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Conv2D(92, (3,3), activation = 'relu',))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(11, activation = 'softmax'))

loss = loss = keras.losses.categorical_crossentropy
optimizer = keras.optimizers.Adam(learning_rate = 1e-3 )
metrics = ['accuracy']

model.compile(optimizer=optimizer, loss=loss,metrics= metrics)

epochs = 8

batch_size = 128

model.fit(X,Y, epochs=epochs, batch_size=batch_size, verbose=2)

model.save('drivingModel4')











