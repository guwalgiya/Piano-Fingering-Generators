import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
from parameters import FINGER_SIZE, N_HIDDEN
class SimpleAttentionModel(Model):
    def __init__(self,
               encoder_hidden_size=N_HIDDEN,
               decoder_hidden_size=N_HIDDEN,
               name='attentionPianoGenerator',
               **kwargs):
        super(SimpleAttentionModel, self).__init__(name=name, **kwargs)
        self.query_seq_encoding = np.array()
        self.rnn = layers.GRU(decoder_hidden_size, return_sequences=True)
        self.attention = layers.Attention()
        self.dense = layers.Dense(FINGER_SIZE, activation='softmax')

    def call(self, inputs):
        attention_weights = self.attention([self.query_seq_encoding, inputs])
        attention_inputs = attention_weights * inputs
        rnn_outs = self.rnn(attention_inputs)
        self.query_seq_encoding = rnn_outs
        return self.dense(rnn_outs)
