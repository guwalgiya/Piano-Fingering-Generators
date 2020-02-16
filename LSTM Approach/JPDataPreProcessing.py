import csv
import os
import pickle
from music21 import pitch
from parameters import BLOCK_LENGTH

DATA_DIR = '../Datasets/JPDataset/'

# make it as [finger, interval, finger, interval, etc]
def toOldFormat():
    train_data_list = []
    train_label_list = []
    temp_list = []
    for _,_, filenames in os.walk(DATA_DIR):
        for filename in sorted(filenames):
            with open(DATA_DIR+filename) as finger_file:
                finger_reader = csv.reader(finger_file)
                pre_finger = -1
                pre_note = -1
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
                            train_data_list.append(list(temp_list))
                            temp_list.append(train_label_list[-1])
                            temp_list[-1], temp_list[-2] = temp_list[-2], temp_list[-1]
                            for _ in range(2): temp_list.pop(0)                                                   
    return train_data_list, train_label_list

def saveDataToPickle(train_data_list, train_label_list):
    pickle.dump(train_data_list, open('../Datasets/processed/train_input_list_4_bi_extra.pkl', 'wb'))
    pickle.dump(train_label_list, open('../Datasets/processed/train_label_list_4_bi_extra.pkl', 'wb'))

train_data_list, train_label_list = toOldFormat()
saveDataToPickle(train_data_list, train_label_list)
