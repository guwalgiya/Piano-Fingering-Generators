import os
from JPDataPreProcessing import getListsFromFilenames
from EvaluateVectorPhrase import main

def evaluate(filenames, gt_dir, est_dir):
    _, gt_finger_list, interval_list, accidental_list = getListsFromFilenames(filenames, gt_dir)
    _, est_finger_list, _, _ = getListsFromFilenames(filenames, est_dir)
    bw_list = [[s, e] for s, e in zip(accidental_list[:-1], accidental_list[1:])]
    num_abs_true, num_abs_false, num_not_ideal = main(interval_list, est_finger_list, bw_list, gt_finger_list)
    print('absolute true: {}'.format(float(num_abs_true) / len(interval_list)))
    print('absolute false: {}'.format(float(num_abs_false) / len(interval_list)))
    print('not ideal: {}'.format(float(num_not_ideal) / len(interval_list)))
   