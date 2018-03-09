import tensorflow as tf
from tensorflow.contrib import rnn
from parameters import *



def getCell(n_hidden):
    return rnn.BasicLSTMCell(n_hidden)

def RNN(x, weights, biases):
    # reshape to [1, n_input]
    x = tf.reshape(x, [-1, N_INPUT])
    # Generate a n_input-element sequence of inputs
    x = tf.split(x,N_INPUT,1)
    # with tf.name_scope('lstm'):
    rnn_cell = rnn.MultiRNNCell([getCell(N_HIDDEN) for _ in range(2)])
    # generate prediction
    outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)
    # there are n_input outputs but
    # we only want the last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

def initNet():
    # tf Graph input
    x = tf.placeholder("float", [None, N_INPUT, 1])
    y = tf.placeholder("float", [None, FINGER_SIZE])
    keep_prob = tf.placeholder(tf.float32)

    # RNN output node weights and biases
    weights = {
        'out': tf.Variable(tf.random_normal([N_HIDDEN, FINGER_SIZE]))
    }
    biases = {
        'out': tf.Variable(tf.random_normal([FINGER_SIZE]))
    }
    return x, y, keep_prob, RNN(x, weights, biases)
