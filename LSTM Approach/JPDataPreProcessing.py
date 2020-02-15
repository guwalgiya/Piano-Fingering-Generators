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
        for filename in filenames:
            with open(DATA_DIR+filename) as finger_file:
                finger_reader = csv.reader(finger_file)
                first_line = finger_reader.__next__()
                pre_note = pitch.Pitch(first_line[3]).ps
                finger = int(first_line[-1].split('_')[0])
                for row in finger_reader:
                    if finger > 0:
                        current_note = pitch.Pitch(row[3]).ps
                        interval = current_note - pre_note
                        pre_note = current_note
                        temp_list.append(finger)
                        temp_list.append(interval)
                        if (len(temp_list) == (BLOCK_LENGTH + 1) * 2):
                            temp_list[-1], temp_list[-2] = temp_list[-2], temp_list[-1]
                            train_label_list.append(temp_list.pop())
                            train_data_list.append(list(temp_list))
                            temp_list.append(train_label_list[-1])
                            temp_list[-1], temp_list[-2] = temp_list[-2], temp_list[-1]
                            for _ in range(2): temp_list.pop(0)   
                    finger = int(row[-1].split('_')[0])        
    return train_data_list, train_label_list

def saveDataToPickle():
    train_data_list, train_label_list = toOldFormat()
    pickle.dump(train_data_list, open('../Datasets/processed/train_input_list_4_bi_extra.pkl', 'wb'))
    pickle.dump(train_label_list, open('../Datasets/processed/train_label_list_4_bi_extra.pkl', 'wb'))

toOldFormat()
saveDataToPickle()
