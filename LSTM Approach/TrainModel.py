import numpy as np
import tensorflow as tf
import time
import pickle
from Utils import elapsed
from LSTM_network import initNet
from parameters import *

# Target log path
logs_path = './logs'
writer = tf.summary.FileWriter(logs_path)

input_list = pickle.load(open("../Datasets/processed/train_input_list.pkl", "rb"))
label_list = pickle.load(open("../Datasets/processed/train_label_list.pkl", "rb"))

x, y, keep_prob, pred = initNet(BIRNN)

# Loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))

optimizer = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE).minimize(cost)

# Model evaluation
correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

tf.summary.scalar('accuracy', accuracy)
tf.summary.scalar('loss', cost)
merged_summary_op = tf.summary.merge_all()
# Initializing the variables
init = tf.global_variables_initializer()

saver = tf.train.Saver()

start_time = time.time()
# Launch the graph
with tf.Session() as session:
    session.run(init)
    step = 0
    offset = 0
    acc_total = 0
    loss_total = 0

    writer.add_graph(session.graph)

    while step < TRAINING_ITERS:
        if offset+1 >= len(input_list):
            offset = 0
            
        symbols_in_keys = input_list[offset]
        symbols_in_keys = np.reshape(np.array(symbols_in_keys), [-1, N_INPUT, 1])

        symbols_out_onehot = np.zeros([FINGER_SIZE], dtype=float)
        symbols_out_onehot[label_list[offset]-1] = 1.0
        symbols_out_onehot = np.reshape(symbols_out_onehot,[1,-1])

        _, acc, loss, onehot_pred, summary = session.run([optimizer, accuracy, cost, pred, merged_summary_op], \
                                                feed_dict={x: symbols_in_keys, y: symbols_out_onehot, keep_prob: 0.5})
        loss_total += loss
        acc_total += acc
        writer.add_summary(summary, step)

        if (step+1) % DISPLAY_STEP == 0:
            print("Iter= " + str(step+1) + ", Average Loss= " + \
                  "{:.6f}".format(loss_total/DISPLAY_STEP) + ", Average Accuracy= " + \
                  "{:.2f}%".format(100*acc_total/DISPLAY_STEP))
            acc_total = 0
            loss_total = 0
            symbols_in = input_list[offset]
            symbols_out = label_list[offset]
            symbols_out_pred = int(tf.argmax(onehot_pred, 1).eval())+1
            print("%s - [%s] vs [%s]" % (symbols_in,symbols_out,symbols_out_pred))
        step += 1
        offset += 1
    if BIRNN:
        saver.save(session, "./models/bi_model/bi_model.ckpt")
    else:
        saver.save(session, "./models/mono_model/model.ckpt")
    print("Optimization Finished!")
    print("Elapsed time: ", elapsed(time.time() - start_time))
    print("Run on command line.")
    print("\ttensorboard --logdir=%s" % (logs_path))
    print("Point your web browser to: http://localhost:6006/")
