import numpy as np
import tensorflow as tf
import pickle
import EvaluatePhrase
from LSTM_network import createModel, initBeam
from Utils import generateNewState, generateNewStateBi
from JPDataPreProcessing import TEST_INPUT_PATH, TEST_LABEL_PATH
from parameters import *

input_list = pickle.load(open(TEST_INPUT_PATH, "rb"))
label_list = pickle.load(open(TEST_LABEL_PATH, "rb"))

model = createModel(BIRNN)
model.load_weights(CHECKPOINT_PATH)

total_absTrue = 0
total_absFalse = 0
total_notGood = 0
total_interval_len = 0

for test_interval, test_finger in zip(input_list, label_list):
    init_state = [test_finger[0], test_interval[0], test_finger[1], test_interval[1], test_finger[2], test_interval[2], test_finger[3], test_interval[3], test_interval[4]]
    
    test_step = 0
    generate_step = len(test_interval)
    temp_finger_res = []
    while test_step < generate_step - (BLOCK_LENGTH):
        np_init_state = np.reshape(np.asarray(init_state, dtype=float), (-1, TIME_STEPS, 1))

        # top_2 = session.run(top_2_holder, feed_dict={onehot_holder: onehot_pred_test[0]})
        # finger_pred_first = top_2[0]+1
        # finger_pred_second = top_2[1]+1

        pred_prob = model.predict(np_init_state)
        finger_pred = int(tf.math.argmax(pred_prob, 1)) + 1

        # finger_pred = int(tf.argmax(onehot_pred_test, 1).eval())+1
        # finger_combo = [init_state[-2], finger_pred_first]
        # if EvaluatePhrase.qualityCheck(init_state[-1], finger_combo):
        #     finger_combo = [init_state[-2], finger_pred_second]
        #     if EvaluatePhrase.qualityCheck(init_state[-1], finger_combo):
        #         finger_pred = finger_pred_first
        #     else:
        #         finger_pred = finger_pred_second
        # else:
        #     finger_pred = finger_pred_first
        
        # finger_combo = [init_state[-3], finger_pred_first]
        # if EvaluatePhrase.qualityCheck(init_state[-2], finger_combo):
        #     finger_combo = [init_state[-3], finger_pred_second]
        #     if EvaluatePhrase.qualityCheck(init_state[-2], finger_combo):
        #         finger_pred = finger_pred_first
        #     else:
        #         finger_pred = finger_pred_second
        # else:
        #     finger_pred = finger_pred_first

        print(str(init_state) + "->" + str(finger_pred))
        temp_finger_res += [finger_pred]
        if test_step < generate_step - BLOCK_LENGTH - 1:
            if BIRNN:
                init_state = generateNewStateBi(init_state, finger_pred, test_interval[test_step+BLOCK_LENGTH+1], False)
            else:
                init_state = generateNewState(init_state, finger_pred, test_interval[test_step+BLOCK_LENGTH], False)
        test_step+=1
    temp_finger_res = [test_finger[-1]] + temp_finger_res
    print('number of notes: '+str(len(temp_finger_res)))
    absTrue, absFalse, notGood = EvaluatePhrase.main(test_interval[BLOCK_LENGTH-1:-1], temp_finger_res, test_finger[BLOCK_LENGTH-1:-1])
    total_absTrue += absTrue
    total_absFalse += absFalse
    total_notGood += notGood
    total_interval_len += (generate_step - (BLOCK_LENGTH-1))
    print('absolute acc: ' + str(absTrue), 'absolute wrong: ' + str(absFalse), 'not ideal: ' + str(notGood))
    print("Testing finished")

print('absolute acc: ' + str(total_absTrue/float(total_interval_len+len(input_list))), \
          'absolute false: ' + str(total_absFalse/float(total_interval_len)), \
          'not ideal: ' + str(total_notGood/float(total_interval_len)))
