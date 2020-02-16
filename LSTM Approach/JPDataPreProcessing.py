import csv
import os
import pickle
from music21 import pitch
from parameters import BLOCK_LENGTH

TRAIN_DATA_DIR = '../Datasets/JPDataset/Train'
TEST_DATA_DIR = '../Datasets/JPDataset/Test'

# make it as [finger, interval, finger, interval, etc]
def toOldTrainFormat():
    train_input_list = []
    train_label_list = []
    for _,_, filenames in os.walk(TRAIN_DATA_DIR):
        for filename in sorted(filenames):
            with open(TRAIN_DATA_DIR+filename) as finger_file:
                finger_reader = csv.reader(finger_file)
                pre_finger = -1
                pre_note = -1
                temp_list = []
                while pre_finger < 0: 
                    first_line = finger_reader.__next__()
                    pre_note = pitch.Pitch(first_line[3]).ps
                    pre_finger = int(first_line[-1].split('_')[0])
                for row in finger_reader:
                    current_finger =  int(row[-1].split('_')[0])
                    if current_finger > 0:
                        temp_list.append(pre_finger)
                        pre_finger = current_finger
                        current_note = pitch.Pitch(row[3]).ps
                        temp_list.append(current_note - pre_note)
                        pre_note = current_note
                        if (len(temp_list) == (BLOCK_LENGTH + 1) * 2):
                            temp_list[-1], temp_list[-2] = temp_list[-2], temp_list[-1]
                            train_label_list.append(temp_list.pop())
                            train_input_list.append(list(temp_list))
                            temp_list.append(train_label_list[-1])
                            temp_list[-1], temp_list[-2] = temp_list[-2], temp_list[-1]
                            for _ in range(2): temp_list.pop(0)                                                   
    return train_input_list, train_label_list

def toOldTestFormat():
    test_input_list = []
    test_label_list = []
    for _, _, filenames in os.walk(TEST_DATA_DIR):
        for filename in sorted(filenames):
            with open(TEST_DATA_DIR+filename) as finger_file:
                finger_reader = csv.reader(finger_file)
                temp_interval_list = []
                temp_finger_list = []
                pre_finger = -1
                pre_note = -1
                while pre_finger < 0: 
                    first_line = finger_reader.__next__()
                    pre_note = pitch.Pitch(first_line[3]).ps
                    pre_finger = int(first_line[-1].split('_')[0])
                for row in finger_reader:
                    current_finger = int(row[-1].split('_')[0])
                    current_note = pitch.Pitch(row[3]).ps
                    if current_finger > 0:
                        temp_interval_list.append(current_note - pre_note)
                        pre_note = current_note
                        temp_finger_list.append(pre_finger)
                        pre_finger = current_finger
                test_input_list.append(list(temp_interval_list))
                test_label_list.append(list(temp_finger_list))
                temp_interval_list.clear()
                temp_finger_list.clear()           
    return test_input_list, test_label_list

def saveDataToPickle(train_input_list, train_label_list, input_path, label_path):
    pickle.dump(train_input_list, open(input_path, 'wb'))
    pickle.dump(train_label_list, open(label_path, 'wb'))

TRAIN_INPUT_PATH = '../Datasets/processed/train_input_list_4_bi_extra.pkl'
TRAIN_LABEL_PATH = '../Datasets/processed/train_label_list_4_bi_extra.pkl'
train_input_list, train_label_list = toOldTrainFormat()
saveDataToPickle(train_input_list, train_label_list, TRAIN_INPUT_PATH, TRAIN_LABEL_PATH)

TEST_INPUT_PATH = '../Datasets/processed/test_input_list_4_bi_extra.pkl'
TEST_LABEL_PATH = '../Datasets/processed/test_label_list_4_bi_extra.pkl'
test_input_list, test_label_list = toOldTestFormat()
saveDataToPickle(test_input_list, test_label_list, TEST_INPUT_PATH, TEST_LABEL_PATH)
