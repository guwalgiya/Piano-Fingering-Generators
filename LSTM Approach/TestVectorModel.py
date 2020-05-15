import pickle
import numpy as np
import tensorflow as tf
import EvaluateVectorPhrase
from NNModelFactory import createBiDirectionModel
from Utils import generateNewVecState, generateNewVecFutureState
from parameters import BLOCK_LENGTH, CHECKPOINT_PATH, FUTURE_LENGTH

def loadModel():
    model = createBiDirectionModel()
    model.load_weights(CHECKPOINT_PATH)
    return model

def testVecModelEval(input_list, label_list, model, verbose=False):
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
        test_interval = [vec[0] for vec in test_vector]
        test_bw = [[vec[1], vec[2]] for vec in test_vector]
        absTrue, absFalse, notGood = EvaluateVectorPhrase.main(test_interval[BLOCK_LENGTH-1:-1], temp_finger_res, test_bw[BLOCK_LENGTH-1:-1], test_finger[BLOCK_LENGTH-1:-1])
        total_absTrue += absTrue
        total_absFalse += absFalse
        total_notGood += notGood
        total_interval_len += (num_intervals - (BLOCK_LENGTH-1))
        if verbose:
            num_note = float(len(temp_finger_res))
            print(f'absolute acc: {absTrue / num_note}, absolute false: {absFalse / num_note}, not ideal: {notGood / num_note}')

    abs_acc = total_absTrue/float(total_interval_len+len(input_list))
    abs_false = total_absFalse/float(total_interval_len)
    not_ideal = total_notGood/float(total_interval_len)
    print('absolute acc: {}, absolute false: {}, not ideal: {}'.format(abs_acc, abs_false, not_ideal))
    return abs_acc, abs_false, not_ideal

def testVecModelSave(input_list, label_list, model):
    for test_vector, test_finger in zip(input_list, label_list):
        init_state = [[test_finger[i]]+test_vector[i] for i in range(BLOCK_LENGTH)]
        num_intervals = len(test_vector)
        temp_finger_res = []
        for test_step in range(0, num_intervals - BLOCK_LENGTH + 1):
            np_init_state = np.reshape(np.asarray(init_state, dtype=float), (-1, BLOCK_LENGTH, 4))
            pred_prob = model.predict(np_init_state)
            finger_pred = int(tf.math.argmax(pred_prob, 1)) + 1
            temp_finger_res += [finger_pred]
            if test_step < num_intervals - BLOCK_LENGTH - 1:
                init_state = generateNewVecState(init_state, finger_pred, test_vector[test_step+BLOCK_LENGTH])
        temp_finger_res = test_finger[0:BLOCK_LENGTH] + temp_finger_res
    return temp_finger_res

def testVecFutureModelSave(input_list, label_list, model):
    for test_vector, test_finger in zip(input_list, label_list):
        init_state_b = [[test_finger[i]]+test_vector[i] for i in range(BLOCK_LENGTH-FUTURE_LENGTH)]
        init_state_a = [[0]+test_vector[i] for i in range(BLOCK_LENGTH-FUTURE_LENGTH, BLOCK_LENGTH)]
        init_state = init_state_b + init_state_a
        num_intervals = len(test_vector)
        temp_finger_res = []
        for test_step in range(0, num_intervals - BLOCK_LENGTH + 1):
            np_init_state = np.reshape(np.asarray(init_state, dtype=float), (-1, BLOCK_LENGTH, 4))
            pred_prob = model.predict(np_init_state)
            finger_pred = int(tf.math.argmax(pred_prob, 1)) + 1
            temp_finger_res += [finger_pred]
            if test_step < num_intervals - BLOCK_LENGTH - 1:
                init_state = generateNewVecFutureState(init_state, finger_pred, test_vector[test_step+BLOCK_LENGTH], FUTURE_LENGTH)
        temp_finger_res = test_finger[0:BLOCK_LENGTH-FUTURE_LENGTH] + temp_finger_res + test_finger[-FUTURE_LENGTH:]
    return temp_finger_res    
    