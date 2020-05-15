import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import regularizers
from AttentionModel import SimpleAttentionModel
from parameters import N_HIDDEN, FINGER_SIZE, FUTURE_LENGTH, BLOCK_LENGTH

def createUniDirectionModel():
    model = tf.keras.Sequential()
    model.add(layers.LSTM(N_HIDDEN))
    model.add(layers.Dense(FINGER_SIZE, activation='softmax'))
    return model

def createBiDirectionModel():
    model = tf.keras.Sequential()
    model.add(layers.Bidirectional(layers.LSTM(N_HIDDEN)))
    model.add(layers.Dense(FINGER_SIZE, activation='softmax'))
    return model

def createBiDirectionWithFutureModel():
    model = tf.keras.Sequential()
    model.add(layers.Bidirectional(layers.LSTM(N_HIDDEN, return_sequences=True)))
    model.add(layers.Lambda(lambda x: x[:, BLOCK_LENGTH-FUTURE_LENGTH-1,:]))
    model.add(layers.Dense(FINGER_SIZE, activation='softmax'))
    return model
    