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
    outputs, _ = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)
    # there are n_input outputs but
    # we only want the last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

def BiRNN(x, weights, biases):
    x = tf.reshape(x, [-1, N_INPUT])
    x = tf.split(x, N_INPUT, 1)
    rnn_cell_fw = rnn.MultiRNNCell([getCell(N_HIDDEN) for _ in range(2)])
    # rnn_cell_fw = getCell(N_HIDDEN)
    rnn_cell_bw = rnn.MultiRNNCell([getCell(N_HIDDEN) for _ in range(2)])
    # rnn_cell_bw = getCell(N_HIDDEN)
    outputs, _, _ = rnn.static_bidirectional_rnn(rnn_cell_fw, rnn_cell_bw, x, dtype=tf.float32)
    return tf.matmul(outputs[-2], weights['out']) + biases['out']

def initBeam():
    one_hot = tf.placeholder("float", [None])
    _, top_2 = tf.nn.top_k(one_hot, 2)
    return one_hot, top_2

def initNet(birnn=False):
    # tf Graph input
    x = tf.placeholder("float", [None, N_INPUT, 1])
    y = tf.placeholder("float", [None, FINGER_SIZE])
    keep_prob = tf.placeholder(tf.float32)

    # RNN output node weights and biases
    biases = {
        'out': tf.Variable(tf.random_normal([FINGER_SIZE]))
    }
    if birnn:
        weights = {'out': tf.Variable(tf.random_normal([N_HIDDEN*2, FINGER_SIZE]))}
    else:
        weights = {'out': tf.Variable(tf.random_normal([N_HIDDEN, FINGER_SIZE]))}

    if birnn:
	print ('init BiRNN')
        return x, y, keep_prob, BiRNN(x, weights, biases)
    else:
    	print ('init RNN')
        return x, y, keep_prob, RNN(x, weights, biases)
