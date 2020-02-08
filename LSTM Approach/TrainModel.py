import numpy as np
import tensorflow as tf
import time
import pickle
from Utils import elapsed
from LSTM_network import initNet
from parameters import *

input_list = pickle.load(open("../Datasets/processed/train_input_list_4_bi.pkl", "rb"))
label_list = pickle.load(open("../Datasets/processed/train_label_list_4_bi.pkl", "rb"))

input_list = np.asarray(input_list, dtype='f')
label_list = np.asarray(label_list)

symbol_input = np.reshape(input_list, (-1, 9, 1))
symbol_one_hot = np.zeros((label_list.size, FINGER_SIZE), dtype=float)
symbol_one_hot[np.arange(label_list.size), label_list-1] = 1.0

model = initNet(BIRNN)
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=[tf.keras.metrics.CategoricalAccuracy()])
model.fit(symbol_input, symbol_one_hot, epochs=10, batch_size=2)
