import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import time
import pickle
from LSTM_network import initNet
from Utils import elapsed, generateNewState
from parameters import *
# import xml_to_midi_for_testing

# # tf Graph input
# x = tf.placeholder("float", [None, N_INPUT, 1])
# y = tf.placeholder("float", [None, FINGER_SIZE])
# keep_prob = tf.placeholder(tf.float32)

# # RNN output node weights and biases
# weights = {
#     'out': tf.Variable(tf.random_normal([N_HIDDEN, FINGER_SIZE]))
# }
# biases = {
#     'out': tf.Variable(tf.random_normal([FINGER_SIZE]))
# }

# def getCell(n_hidden):
#     return rnn.BasicLSTMCell(n_hidden)

# def RNN(x, weights, biases):
#     # reshape to [1, n_input]
#     x = tf.reshape(x, [-1, N_INPUT])
#     # Generate a n_input-element sequence of inputs
#     x = tf.split(x,N_INPUT,1)
#     # with tf.name_scope('lstm'):
#     rnn_cell = rnn.MultiRNNCell([getCell(N_HIDDEN) for _ in range(2)])
#     # generate prediction
#     outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)
#     # there are n_input outputs but
#     # we only want the last output
#     return tf.matmul(outputs[-1], weights['out']) + biases['out']

# pred = RNN(x, weights, biases)

input_list = pickle.load(open("../Datasets/processed/test_input_list.pkl", "rb"))
label_list = pickle.load(open("../Datasets/processed/test_label_list.pkl", "rb"))

x, _, keep_prob, pred = initNet()

init = tf.global_variables_initializer()

saver = tf.train.Saver()

start_time = time.time()
# Launch the graph
with tf.Session() as session:
    # test_interval = [2,2,1,2,2,2,1,-1,-2,-2,-2,-1,-2,-2]
    # test_interval = [intv/12.0 for intv in test_interval]
    # saver.restore(session,"./models/model.ckpt") 
    # test_finger = [1,2,3,5,4,2,3,4,5,2,1,1,2,4,5,4,3,2,1]
    # init_state = [1/5.0,test_interval[0],2/5.0,test_interval[1],3/5.0,test_interval[2],1/5.0,test_interval[3]]
    # print(init_state)
    # test_step = 0
    # generate_step = len(test_interval)
    # while test_step < generate_step - 4:
    #     np_init_state = np.reshape(np.array(init_state), [-1, N_INPUT, 1])
    #     onehot_pred_test = session.run(pred, feed_dict={x: np_init_state, keep_prob: 1})
    #     finger_pred = int(tf.argmax(onehot_pred_test, 1).eval())+1
    #     print(str(init_state) + "->" + str(finger_pred))
    #     # init_state = init_state[2:] + [test_finger[test_step+4],test_interval[test_step+4]]
    #     init_state = generateNewState(init_state, finger_pred, test_interval[test_step+4])
    #     test_step+=1
    # print("Elapsed time: ", elapsed(time.time() - start_time))
    # print("Testing finished")
    saver.restore(session, "./models/model.ckpt")
    for i in range(len(input_list)):
        test_interval = input_list[i]
        test_finger = label_list[i]
        init_state = [test_finger[0], test_interval[0], test_finger[1], test_interval[1], test_finger[2], test_interval[2], test_finger[3], test_interval[3]]
        test_step = 0
        generate_step = len(test_interval)
        while test_step < generate_step - 4:
            np_init_state = np.reshape(np.array(init_state), [-1, N_INPUT, 1])
            onehot_pred_test = session.run(pred, feed_dict={x: np_init_state, keep_prob: 1})
            finger_pred = int(tf.argmax(onehot_pred_test, 1).eval())+1
            print(str(init_state) + "->" + str(finger_pred))
            init_state = generateNewState(init_state, finger_pred, test_interval[test_step+4])
            test_step+=1
        print("Elapsed time: ", elapsed(time.time() - start_time))
        print("Testing finished")
