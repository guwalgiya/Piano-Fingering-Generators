import csv
import os
import pickle
import numpy as np
from music21 import pitch
from parameters import BLOCK_LENGTH
from Utils import slide_window_gen

# make it as [finger, interval, finger, interval, etc]
def toInterleavedTrainFormat(filenames, data_dir):
    train_input_list = []
    train_label_list = []
    for filename in sorted(filenames):
        with open(data_dir+filename) as finger_file:
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

# make input_list as all intervals and test_label as all fingers
def toInterleavedTestFormat(filenames, data_dir):
    test_input_list = []
    test_label_list = []
    for filename in sorted(filenames):
        with open(data_dir+filename) as finger_file:
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
            temp_finger_list.append(current_finger)
            test_label_list.append(list(temp_finger_list))
            temp_interval_list.clear()
            temp_finger_list.clear()           
    return test_input_list, test_label_list

# train_input_list has shape: [[f, i, b/w, b/w], [f, i, b/w, b/w], ...], train_label_list has shape: [f, f, f....]
def toVectorTrainFormat(filenames, data_dir):
    train_input_list = []
    train_label_list = []
    for filename in sorted(filenames):
        with open(data_dir + filename, 'r') as finger_file:
            finger_reader = csv.reader(finger_file)
            finger_list = []
            note_list = []
            accidental_list = []
            for row in finger_reader:
                current_finger = int(row[-1].split('_')[0])
                current_note = pitch.Pitch(row[3]).ps
                borw =int(pitch.Pitch(row[3]).accidental == None)
                if current_finger > 0:
                    finger_list.append(current_finger)
                    note_list.append(current_note)
                    accidental_list.append(borw)
            interval_list = np.diff(np.array(note_list, dtype=int)).tolist()
            vector_list = [[f, i, bw_s, bw_e] for f, i, bw_s, bw_e in zip(finger_list[:-1], interval_list, accidental_list[:-1], accidental_list[1:])]
            train_input_list.extend([l for l in slide_window_gen(vector_list, BLOCK_LENGTH)])
            train_label_list.extend([f for f in finger_list[BLOCK_LENGTH:]])
    return train_input_list, train_label_list


# for each file, test_input has shape: [[i, b/w, b/w], ...], test_label has shape: [f, f, f, f....]
def toVectorTestFormat(filenames, data_dir):
    test_input_list = []
    test_label_list = []
    for filename in sorted(filenames):
        with open(data_dir + filename, 'r') as finger_file:
            finger_reader = csv.reader(finger_file)
            finger_list = []
            note_list = []
            accidental_list = []
            for row in finger_reader:
                current_finger = int(row[-1].split('_')[0])
                current_note = pitch.Pitch(row[3]).ps
                borw =int(pitch.Pitch(row[3]).accidental == None)
                if current_finger > 0:
                    finger_list.append(current_finger)
                    note_list.append(current_note)
                    accidental_list.append(borw)
            interval_list = np.diff(np.array(note_list, dtype=int)).tolist()
            vector_list = [[i, bw_s, bw_e] for i, bw_s, bw_e in zip(interval_list, accidental_list[:-1], accidental_list[1:])]
            test_input_list.append(vector_list)
            test_label_list.append(finger_list)
    return test_input_list, test_label_list

def getBwList(filenames, data_dir):
    bw_list = []
    for filename in sorted(filenames):
        with open(data_dir + filename, 'r') as finger_file:
            finger_reader = csv.reader(finger_file)
            accidental_list = []
            for row in finger_reader:
                current_finger = int(row[-1].split('_')[0])
                borw =int(pitch.Pitch(row[3]).accidental == None)
                if current_finger > 0:
                    accidental_list.append(borw)
            bw_s = accidental_list[:-1]
            bw_e = accidental_list[1:]
            for s, e in zip(bw_s, bw_e):
                bw_list.append([s, e])
    return bw_list
