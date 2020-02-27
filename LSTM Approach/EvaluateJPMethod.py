import os
from JPDataPreProcessing import toOldTestFormat
from EvaluatePhrase import main

GT_DIR = '../Datasets/JPDataset/'
EST_DIR = '../Datasets/JPESTResults/'
def getFileNames():
    gt_filenames = []
    est_filenames = []
    for _, _, filenames in os.walk(GT_DIR):
        gt_filenames = filenames
    for _, _, filenames in os.walk(EST_DIR):
        est_filenames = filenames
    return gt_filenames, est_filenames

def evaluate(gt_filenames, est_filenames):
    interval_list, gt_finger_list = toOldTestFormat(gt_filenames, GT_DIR)
    _, est_finger_list = toOldTestFormat(est_filenames, EST_DIR)
    total_true = 0
    total_false = 0
    total_nideal = 0
    for interval, est_finger, gt_finger in zip(interval_list, est_finger_list, gt_finger_list):
        num_abs_true, num_abs_false, num_not_good = main(interval, est_finger, gt_finger)
        total_true += float(num_abs_true) / len(gt_finger)
        total_false += float(num_abs_false) / len(gt_finger)
        total_nideal += float(num_not_good) / len(gt_finger)
        # print('absolute true: {}'.format(float(num_abs_true) / len(gt_finger)))
        # print('absolute false: {}'.format(float(num_abs_false) / len(gt_finger)))
        # print('not ideal: {}'.format(float(num_not_good) / len(gt_finger)))
        
    print('absolute true: {}'.format(float(total_true) / len(interval_list)))
    print('absolute false: {}'.format(float(total_false) / len(interval_list)))
    print('not ideal: {}'.format(float(total_nideal) / len(interval_list)))
gt_filenames, est_filenames = getFileNames()
evaluate(gt_filenames, est_filenames)
   