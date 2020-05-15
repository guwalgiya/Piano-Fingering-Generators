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

def SplitDataExcludeBachTestOnMozart(data_dir):
    bach_prefix = ['001','002','003','004','005','006','007','008','009','010','032','033','041','042','043','044','045','046','047','048','049','050']
    for _, _, filenames in os.walk(data_dir):
        filenames = sorted(filenames)
        test_files = filenames[41:51]
        train_files = []
        for filename in filenames[100:]:
            if filename.split('-')[0] not in bach_prefix:
                train_files.append(filename)
    return train_files, test_files

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