import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
from parameters import FINGER_SIZE, N_HIDDEN
class SimpleAttentionModel(Model):
    def __init__(self,
               rnn_hidden_size=N_HIDDEN,
               dense_hidden_size=int(N_HIDDEN/2),
               name='attentionPianoGenerator',
               **kwargs):
        super(SimpleAttentionModel, self).__init__(name=name, **kwargs)
        self.rnn = layers.GRU(rnn_hidden_size, return_sequences=True, return_state=True)
        self.attention = layers.Attention()
        self.dense = layers.Dense(N_HIDDEN/2, activation='relu')
        self.softmax = layers.Dense(FINGER_SIZE, activation='softmax')

    def call(self, inputs):
        rnn_sequences, final_hidden_state = self.rnn(inputs)
        attention_weights = self.attention([final_hidden_state, rnn_sequences])
        context_vec = layers.GlobalAveragePooling1D()(attention_weights)
        concatenated_vec = layers.Concatenate()([final_hidden_state, context_vec])
        final_vec = self.dense(concatenated_vec)
        return self.softmax(final_vec)
