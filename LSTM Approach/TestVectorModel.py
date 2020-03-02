import pickle
import numpy as np
import tensorflow as tf
import EvaluateVectorPhrase
from LSTM_network import createModel, initBeam
from Utils import generateNewVecState
from parameters import *

def loadModel():
    model = createModel(BIRNN)
    model.load_weights(CHECKPOINT_PATH)
    return model

def testVecModel(input_list, label_list, model):
    total_absTrue = 0
    total_absFalse = 0
    total_notGood = 0
    total_interval_len = 0

    for test_vector, test_finger in zip(input_list, label_list):
        init_state = [[test_finger[i]]+test_vector[i] for i in range(BLOCK_LENGTH)]
        num_intervals = len(test_vector)
        temp_finger_res = []
        for test_step in range(0, num_intervals - BLOCK_LENGTH):
            np_init_state = np.reshape(np.asarray(init_state, dtype=float), (-1, BLOCK_LENGTH, 4))
            pred_prob = model.predict(np_init_state)
            finger_pred = int(tf.math.argmax(pred_prob, 1)) + 1
            temp_finger_res += [finger_pred]
            if test_step < num_intervals - BLOCK_LENGTH - 1:
                init_state = generateNewVecState(init_state, finger_pred, test_vector[test_step+BLOCK_LENGTH])

        temp_finger_res = [test_finger[-1]] + temp_finger_res
        print('number of notes: '+str(len(temp_finger_res)))
        test_interval = [vec[0] for vec in test_vector]
        test_bw = [[vec[1], vec[2]] for vec in test_vector]
        absTrue, absFalse, notGood = EvaluateVectorPhrase.main(test_interval[BLOCK_LENGTH-1:-1], temp_finger_res, test_bw[BLOCK_LENGTH-1:-1], test_finger[BLOCK_LENGTH-1:-1])
        total_absTrue += absTrue
        total_absFalse += absFalse
        total_notGood += notGood
        total_interval_len += (num_intervals - (BLOCK_LENGTH-1))
        print('absolute acc: ' + str(absTrue), 'absolute wrong: ' + str(absFalse), 'not ideal: ' + str(notGood))

    print('absolute acc: ' + str(total_absTrue/float(total_interval_len+len(input_list))), \
            'absolute false: ' + str(total_absFalse/float(total_interval_len)), \
            'not ideal: ' + str(total_notGood/float(total_interval_len)))
