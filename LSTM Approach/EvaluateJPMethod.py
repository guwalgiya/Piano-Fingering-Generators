import os
from JPDataPreProcessing import getListsFromFilenames
from EvaluateVectorPhrase import main

def evaluate(filenames, gt_dir, est_dir):
    _, gt_finger_list, interval_list, accidental_list = getListsFromFilenames(filenames, gt_dir)
    _, est_finger_list, _, _ = getListsFromFilenames(filenames, est_dir)
    total_true = 0
    total_false = 0
    total_nideal = 0
    for interval, est_finger, gt_finger in zip(interval_list, est_finger_list, gt_finger_list):
        num_abs_true, num_abs_false, num_not_good = main(interval, est_finger, accidental_list, gt_finger)
        total_true += float(num_abs_true) / len(gt_finger)
        total_false += float(num_abs_false) / len(gt_finger)
        total_nideal += float(num_not_good) / len(gt_finger)
    print('absolute true: {}'.format(float(total_true) / len(interval_list)))
    print('absolute false: {}'.format(float(total_false) / len(interval_list)))
    print('not ideal: {}'.format(float(total_nideal) / len(interval_list)))
   