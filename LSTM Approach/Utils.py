import os
import random
import pickle

def elapsed(sec):
    if sec<60:
        return str(sec) + " sec"
    elif sec<(60*60):
        return str(sec/60) + " min"
    else:
        return str(sec/(60*60)) + " hr"

def SplitChopinData(data_dir):
    for _,_, filenames in os.walk(data_dir):
        filenames_ = sorted(filenames)
        test_files = filenames_[100:150]
        train_files = filenames_[150:] + filenames_[0 : 99]
    pre_prefix = ''
    hmm_files = []
    for test_file in test_files:
        prefix = test_file.split('-')[0]
        if prefix != pre_prefix:
            hmm_files.append(test_file)
            pre_prefix = prefix
    return train_files, test_files, hmm_files

def SplitMozartData(data_dir):
    for _,_, filenames in os.walk(data_dir):
        filenames_ = sorted(filenames)
        test_files = filenames_[40:100]
        train_files = filenames_[0:40] + filenames_[100:]
    pre_prefix = ''
    hmm_files = []
    for test_file in test_files:
        prefix = test_file.split('-')[0]
        if prefix != pre_prefix:
            hmm_files.append(test_file)
            pre_prefix = prefix
    return train_files, test_files, hmm_files

def SplitBachData(data_dir):
    for _,_, filenames in os.walk(data_dir):
        filenames_ = sorted(filenames)
        test_files = filenames_[0:40]
        train_files = filenames_[40:]
    pre_prefix = ''
    hmm_files = []
    for test_file in test_files:
        prefix = test_file.split('-')[0]
        if prefix != pre_prefix:
            hmm_files.append(test_file)
            pre_prefix = prefix
    return train_files, test_files, hmm_files

def SplitJPData(data_dir, hmm_res_dir):
    for _, _, filenames in os.walk(data_dir):
        filenames_ = sorted(filenames)
        test_files = filenames_[0:150]
        train_files = filenames_[150:]
    for _, _, filenames in os.walk(hmm_res_dir):
        hmm_res_files = sorted(filenames)
    return train_files, test_files, hmm_res_files

def shuffleDataset(split_ratio, data_dir):
    for _, _, filenames in os.walk(data_dir):
        random.shuffle(filenames)
        num_train_files = int(len(filenames) * split_ratio)
        train_files = filenames[:num_train_files]
        test_files = filenames[num_train_files:]
        return train_files, test_files

def saveToPickle(data, path):
    pickle.dump(data, open(path, 'wb'))

def loadFromPickle(data_path):
    return pickle.load(open(data_path, "rb"))

def generateNewState(old_state, finger_pred, new_interval, normalization=True):
    if normalization:
        return old_state[2:]+[finger_pred/5.0, new_interval]
    else:
        return old_state[2:]+[finger_pred, new_interval]
    
def generateNewStateBi(old_state, finger_pred, new_interval, normalization=True):
    if normalization:
        return old_state[2:-1] + [finger_pred/5.0, old_state[-1], new_interval]
    else:
        return old_state[2:-1] + [finger_pred, old_state[-1], new_interval]

def generateNewVecState(old_state, finger_pred, new_vec):
    return old_state[1:] + [[finger_pred]+new_vec]     

def generateNewVecFutureState(old_state, finger_pred, new_vec, future_size):
    pred = old_state[-future_size]
    pred[0] = finger_pred
    old_state[-future_size] = pred
    return old_state[1:] + [[0]+new_vec]

def slide_window_gen(input_list, window_size):
    for start in range(len(input_list) - window_size + 1):
        yield input_list[start : start + window_size]

def slide_window_future_gen(input_list, window_size, future_size):
    for start in range(len(input_list) - window_size + 1):
        full_list = input_list[start : start + window_size]
        for i in range(window_size-future_size, window_size):
            full_list[i][0] = 0
        yield full_list