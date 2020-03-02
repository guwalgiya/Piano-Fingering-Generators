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

def slide_window_gen(input_list, window_size):
    for start in range(len(input_list) - window_size + 1):
        yield input_list[start : start + window_size]