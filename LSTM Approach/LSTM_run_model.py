import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import time
import pickle
import DataPreprocess
import GetTrainData
# import xml_to_midi_for_testing
# from music21 import converter


def elapsed(sec):
    if sec<60:
        return str(sec) + " sec"
    elif sec<(60*60):
        return str(sec/60) + " min"
    else:
        return str(sec/(60*60)) + " hr"


# Target log path
logs_path = './logs'
writer = tf.summary.FileWriter(logs_path)

input_list = pickle.load(open("../Datasets/processed/input_list.pkl", "rb"))
label_list = pickle.load(open("../Datasets/processed/label_list.pkl", "rb"))
# block_length = 4
# training_path = '../Datasets/Czerny_599_with_Fingering'
# book_interval, book_finger = DataPreprocess.main(training_path)
# input_list, label_list = GetTrainData.main(book_interval, book_finger, block_length)

def generateNewState(old_state, finger_pred, new_interval):
    return old_state[2:]+[finger_pred, new_interval]


# test_interval, first_input = getTestData()

# Parameters
learning_rate = 0.001
training_iters = 60000
display_step = 1000
n_input = 8
n_phrase = len(input_list)
finger_size = 5
# number of units in RNN cell
n_hidden = 256

# tf Graph input
x = tf.placeholder("float", [None, n_input, 1])
y = tf.placeholder("float", [None, finger_size])
keep_prob = tf.placeholder(tf.float32)

# RNN output node weights and biases
weights = {
    'out': tf.Variable(tf.random_normal([n_hidden, finger_size]))
}
biases = {
    'out': tf.Variable(tf.random_normal([finger_size]))
}

def getCell(n_hidden):
    return rnn.BasicLSTMCell(n_hidden)

def RNN(x, weights, biases):

    # reshape to [1, n_input]
    x = tf.reshape(x, [-1, n_input])
    

    # Generate a n_input-element sequence of inputs
    x = tf.split(x,n_input,1)

    # with tf.name_scope('lstm'):
    rnn_cell = rnn.MultiRNNCell([getCell(n_hidden) for _ in range(2)])

    # generate prediction
    outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)

    # there are n_input outputs but
    # we only want the last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

pred = RNN(x, weights, biases)

# Loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))

# optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Model evaluation
correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
tf.summary.scalar('accuracy', accuracy)
tf.summary.scalar('loss', cost)
merged_summary_op = tf.summary.merge_all()
# Initializing the variables
init = tf.global_variables_initializer()


# saver = tf.train.Saver()
start_time = time.time()
# Launch the graph
with tf.Session() as session:
    session.run(init)
    step = 0
    offset = 0
    acc_total = 0
    loss_total = 0
    test_interval = [2,2,1,2,2,2,1,-1,-2,-2,-2,-1,-2,-2]
    # generate_step = len(test_interval) - 2

    writer.add_graph(session.graph)

    while step < training_iters:
        # Generate a minibatch. Add some randomness on selection process.
        if offset+1 >= n_phrase:
            offset = 0
            
        symbols_in_keys = input_list[offset]
        symbols_in_keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])

        symbols_out_onehot = np.zeros([finger_size], dtype=float)
        symbols_out_onehot[label_list[offset]-1] = 1.0
        symbols_out_onehot = np.reshape(symbols_out_onehot,[1,-1])

        _, acc, loss, onehot_pred, summary = session.run([optimizer, accuracy, cost, pred, merged_summary_op], \
                                                feed_dict={x: symbols_in_keys, y: symbols_out_onehot, keep_prob: 0.5})
        loss_total += loss
        acc_total += acc
        writer.add_summary(summary, step)
        # tf.summary.scalar('loss', loss)
        # tf.summary.scalar('accuracy', acc)
        if (step+1) % display_step == 0:
            print("Iter= " + str(step+1) + ", Average Loss= " + \
                  "{:.6f}".format(loss_total/display_step) + ", Average Accuracy= " + \
                  "{:.2f}%".format(100*acc_total/display_step))
            acc_total = 0
            loss_total = 0
            symbols_in = input_list[offset]
            symbols_out = label_list[offset]
            symbols_out_pred = int(tf.argmax(onehot_pred, 1).eval())+1
            print("%s - [%s] vs [%s]" % (symbols_in,symbols_out,symbols_out_pred))
        step += 1
        offset += 1
    # saver.save(session, "./Model/model") 
    test_finger = [1,2,3,5,4,2,3,4,5,2,1,1,2,4,5,4,3,2,1]
    # interval_test = test_interval[0:len(test_finger)]
    init_state = [2,test_interval[0],1,test_interval[1],2,test_interval[2],3,test_interval[3]]
    test_step = 0
    generate_step = len(test_interval)
    while test_step < generate_step - 4:
        np_init_state = np.reshape(np.array(init_state), [-1, n_input, 1])
        onehot_pred_test = session.run(pred, feed_dict={x: np_init_state, keep_prob: 1})
        finger_pred = int(tf.argmax(onehot_pred_test, 1).eval())+1
        print(str(init_state) + "->" + str(finger_pred))
        # init_state = init_state[2:] + [test_finger[test_step+4],test_interval[test_step+4]]
        init_state = generateNewState(init_state, finger_pred, test_interval[test_step+4])
        test_step+=1
    # test_step = 0
    # init_state = first_input
    # while test_step < generate_step:
    #     np_init_state = np.reshape(np.array(init_state), [-1, n_input, 1])
    #     onehot_pred_test = session.run(pred, feed_dict={x: np_init_state})
    #     finger_pred = int(tf.argmax(onehot_pred_test, 1).eval())+1
    #     print(str(init_state) + "->" + str(finger_pred))
    #     init_state = generateNewState(init_state, finger_pred, test_interval[test_step+2])
    #     test_step += 1
    print("Optimization Finished!")
    print("Elapsed time: ", elapsed(time.time() - start_time))
    print("Run on command line.")
    print("\ttensorboard --logdir=%s" % (logs_path))
    print("Point your web browser to: http://localhost:6006/")