import tensorflow as tf
from tensorflow.keras import layers
from parameters import N_HIDDEN, FINGER_SIZE

def initBeam():
    one_hot = tf.placeholder("float", [None])
    _, top_2 = tf.nn.top_k(one_hot, 2)
    return one_hot, top_2

def createModel(birnn=False):
    model = tf.keras.Sequential()
    if birnn:
        model.add(layers.LSTM(N_HIDDEN))
    else:
        model.add(layers.Bidirectional(layers.LSTM(N_HIDDEN)))
    model.add(layers.Dense(FINGER_SIZE, activation='softmax'))
    return model