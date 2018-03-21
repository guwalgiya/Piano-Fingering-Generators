import numpy as np
import tensorflow as tf
# from tensorflow.contrib import rnn
import time
import pickle
import evaluatePhrase
from LSTM_network import initNet
from Utils import elapsed, generateNewState
from parameters import *

input_list = pickle.load(open("../Datasets/processed/test_input_list.pkl", "rb"))
label_list = pickle.load(open("../Datasets/processed/test_label_list.pkl", "rb"))

x, _, keep_prob, pred = initNet(BIRNN)

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
    if BIRNN:
    	saver.restore(session, "./models/bi_model/bi_model.ckpt")
    else:
    	saver.restore(session, "./models/mono_model/model.ckpt")
    total_absTrue = 0
    total_absFalse = 0
    total_notGood = 0
    total_interval_len = 0
    for i in range(len(input_list)):
        test_interval = input_list[i]
        test_finger = label_list[i]
        init_state = [test_finger[0], test_interval[0], test_finger[1], test_interval[1], test_finger[2], test_interval[2], test_finger[3], test_interval[3]]
        test_step = 0
        generate_step = len(test_interval)
        temp_finger_res = []
        while test_step < generate_step - 3:
            np_init_state = np.reshape(np.array(init_state), [-1, N_INPUT, 1])
            onehot_pred_test = session.run(pred, feed_dict={x: np_init_state, keep_prob: 1})
            finger_pred = int(tf.argmax(onehot_pred_test, 1).eval())+1
            print(str(init_state) + "->" + str(finger_pred))
            temp_finger_res += [finger_pred]
            if test_step < generate_step - 4:
                init_state = generateNewState(init_state, finger_pred, test_interval[test_step+4], False)
            test_step+=1
        temp_finger_res = [test_finger[3]] + temp_finger_res
        print(len(temp_finger_res))
        absTrue, absFalse, notGood = evaluatePhrase.main(test_interval[3:], temp_finger_res, test_finger[3:])
        total_absTrue += absTrue
        total_absFalse += absFalse
        total_notGood += notGood
        total_interval_len += (generate_step - 3)
        print(absTrue, absFalse, notGood)
        print("Elapsed time: ", elapsed(time.time() - start_time))
        print("Testing finished")
    print(total_absTrue/float(total_interval_len+len(input_list)), total_absFalse/float(total_interval_len), total_notGood/float(total_interval_len)) 
