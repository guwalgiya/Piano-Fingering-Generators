import csv
import os
import math
import pickle
import itertools
import numpy as np
from music21 import pitch
from parameters import BLOCK_LENGTH, FUTURE_LENGTH
from Utils import slide_window_gen, slide_window_future_gen

# treat left/right hand seperatly, only take right hand here
def getListsFromSingeFile(filename, data_dir):
    note_list = []
    finger_list = []
    accidental_list = []
    id_list = []
    with open(data_dir+filename) as finger_file:
        reader = csv.reader(finger_file)
        pre_onset = 0
        for row in reader:
            current_onset = float(row[1])
            current_finger = int(row[-1].split('_')[0])
            current_note = pitch.Pitch(row[3]).ps
            borw =int(pitch.Pitch(row[3]).accidental == None) # 1 if white, 0 if black
            if (current_finger > 0 and not math.isclose(pre_onset, current_onset, rel_tol=1e-4)):
                note_list.append(current_note)
                finger_list.append(current_finger)
                accidental_list.append(borw)
                id_list.append(int(row[0]))
            pre_onset = current_onset
        interval_list = np.diff(np.array(note_list, dtype=int)).tolist()
    return note_list, finger_list, interval_list, accidental_list, id_list

def getListsFromFilenames(filenames, data_dir):
    note_list = []
    finger_list = []
    interval_list = []
    accidental_list = []
    id_list = []
    for filename in sorted(filenames):
        n, f, i, a, _id = getListsFromSingeFile(filename, data_dir)
        note_list.extend(n)
        finger_list.extend(f)
        interval_list.extend(i)
        accidental_list.extend(a)
        id_list.extend(id_list)
    return note_list, finger_list, interval_list, accidental_list

# make each row has [finger, interval, finger, interval, etc]
def toInterleavedTrainFormat(filenames, data_dir):
    train_input_list = []
    train_label_list = []
    for filename in sorted(filenames):  
        _, finger_list, interval_list, _, _ = getListsFromSingeFile(filename, data_dir)
        interleaved_row = [list(itertools.chain.from_iterable(zip(finger_slot, interval_slot))) for finger_slot, interval_slot in zip(slide_window_gen(finger_list, BLOCK_LENGTH), slide_window_gen(interval_list, BLOCK_LENGTH))]
        train_input_list.extend(interleaved_row)
        train_label_list.extend([f for f in finger_list[BLOCK_LENGTH:]])
    return train_input_list, train_label_list

# make input_list as all intervals and test_label as all fingers
def toInterleavedTestFormat(filenames, data_dir):
    test_input_list = []
    test_label_list = []
    for filename in sorted(filenames):  
        _, finger_list, interval_list, _, _ = getListsFromSingeFile(filename, data_dir)
        test_input_list.append(finger_list)
        test_label_list.append(interval_list)
    return test_input_list, test_label_list

# train_input_list has shape: [[f, i, b/w, b/w], [f, i, b/w, b/w], ...], train_label_list has shape: [f, f, f....]
def toVectorTrainFormat(filenames, data_dir):
    train_input_list = []
    train_label_list = []
    for filename in sorted(filenames):
        _, finger_list, interval_list, accidental_list, _ = getListsFromSingeFile(filename, data_dir)
        vector_list = [[f, i, bw_s, bw_e] for f, i, bw_s, bw_e in zip(finger_list[:-1], interval_list, accidental_list[:-1], accidental_list[1:])]
        train_input_list.extend([l for l in slide_window_gen(vector_list, BLOCK_LENGTH)])
        train_label_list.extend([f for f in finger_list[BLOCK_LENGTH:]])
    return train_input_list, train_label_list

# for each file, test_input has shape: [[i, b/w, b/w], ...], test_label has shape: [f, f, f, f....]
def toVectorTestFormat(filenames, data_dir):
    test_input_list = []
    test_label_list = []
    test_id_list = []
    for filename in sorted(filenames):
        _, finger_list, interval_list, accidental_list, id_list = getListsFromSingeFile(filename, data_dir)
        vector_list = [[i, bw_s, bw_e] for i, bw_s, bw_e in zip(interval_list, accidental_list[:-1], accidental_list[1:])]
        test_input_list.append(vector_list)
        test_label_list.append(finger_list)
        test_id_list.append(id_list)
    return test_input_list, test_label_list, test_id_list

def toVectorFutureTrainFormat(filenames, data_dir):
    train_input_list = []
    train_label_list = []
    for filename in sorted(filenames):
        _, finger_list, interval_list, accidental_list, _ = getListsFromSingeFile(filename, data_dir)
        vector_list = [[f, i, bw_s, bw_e] for f, i, bw_s, bw_e in zip(finger_list[:-1], interval_list, accidental_list[:-1], accidental_list[1:])]
        train_input_list.extend([l for l in slide_window_future_gen(vector_list, BLOCK_LENGTH, FUTURE_LENGTH)])
        train_label_list.extend([f for f in finger_list[BLOCK_LENGTH-FUTURE_LENGTH:-FUTURE_LENGTH]])
    return train_input_list, train_label_list
        
