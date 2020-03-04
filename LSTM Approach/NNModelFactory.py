import tensorflow as tf
from tensorflow.keras import layers
from parameters import N_HIDDEN, FINGER_SIZE

def createUniDirectionModel():
    model = tf.keras.Sequential()
    model.add(layers.LSTM(N_HIDDEN))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(FINGER_SIZE, activation='softmax'))
    return model

def createBiDirectionModel():
    model = tf.keras.Sequential()
    model.add(layers.Bidirectional(layers.LSTM(N_HIDDEN)))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(FINGER_SIZE, activation='softmax'))
    return model
    