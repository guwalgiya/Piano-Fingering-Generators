import os
from JPDataPreProcessing import getListsFromFilenames, getListsFromSingeFile
from EvaluateVectorPhrase import main

def evaluate_yz(filenames, gt_dir, est_dir):
    for filename in filenames:
        print(filename + ': ')
        _, gt_finger_list, interval_list, accidental_list, gt_id_list = getListsFromSingeFile(filename, gt_dir)
        _, est_finger_list, _, _, est_id_list = getListsFromSingeFile(filename, est_dir)
        
        gt_align_idx, est_align_idx = _align_sequence(gt_id_list, est_id_list)
        gt_aligned_finger = [gt_finger_list[i] for i in gt_align_idx]
        accidental_aligned_list = [accidental_list[i] for i in gt_align_idx]
        est_aligned_finger = [est_finger_list[i] for i in est_align_idx]
        interval_aligned_list = [interval_list[i] for i in gt_align_idx[:-1]]
        bw_list = [[s, e] for s, e in zip(accidental_aligned_list[:-1], accidental_aligned_list[1:])]
        num_abs_true, num_abs_false, num_not_ideal = main(interval_aligned_list, est_aligned_finger, bw_list, gt_aligned_finger)
        
        print('absolute true: {}'.format(float(num_abs_true) / len(interval_list)))
        print('absolute false: {}'.format(float(num_abs_false) / len(interval_list)))
        print('not ideal: {}'.format(float(num_not_ideal) / len(interval_list)))

def evaluate_yz_single(filename, gt_dir, est_finger_list):
    _, gt_finger_list, interval_list, accidental_list, _ = getListsFromSingeFile(filename, gt_dir)
    bw_list = [[s, e] for s, e in zip(accidental_list[:-1], accidental_list[1:])]
    num_abs_true, num_abs_false, num_not_ideal = main(interval_list, est_finger_list, bw_list, gt_finger_list)
    print('absolute true: {}'.format(float(num_abs_true) / len(interval_list)))
    print('absolute false: {}'.format(float(num_abs_false) / len(interval_list)))
    print('not ideal: {}'.format(float(num_not_ideal) / len(interval_list)))

def evaluate_jp(filenames, gt_dir, res_finger_list, res_id_list):
    gt_finger_lists = []
    gt_id_lists = []
    for filename in filenames:
        _, gt_finger_list, _, _, gt_id_list = getListsFromSingeFile(filename, gt_dir)
        gt_finger_lists.append(gt_finger_list)
        gt_id_lists.append(gt_id_list)
    M_gen, M_high, M_soft = _evaluate_jp(res_finger_list, gt_finger_lists, res_id_list, gt_id_lists)
    return M_gen, M_high, M_soft

def _evaluate_jp(res_finger_list, gt_finger_lists, res_id_list, gt_id_lists):
    rate_list = []
    piece_len = len(res_finger_list)
    soft_list = [0] * len(res_finger_list)
    for gt_finger_list, gt_id_list in zip(gt_finger_lists, gt_id_lists):
        match_list = _find_join_set_then_match(res_id_list, gt_id_list, res_finger_list, gt_finger_list)
        match_count = match_list.count(1) 
        rate_list.append(match_count)
        for i in range(len(match_list)):
            if (match_list[i] == 1):
                soft_list[i] = 1
    soft_count = soft_list.count(1)
    rate_list = [ rate / float(piece_len) for rate in rate_list ]
    return sum(rate_list) / float(len(rate_list)), max(rate_list), soft_count / float(piece_len)
    
def _align_sequence(A, B):
    aligned_A = [] # list of idxs
    aligned_B = [] # list of idxs
    i = 0
    j = 0
    while (i < len(A) and j < len(B)):
        if (A[i] == B[j]):
            aligned_A.append(i)
            aligned_B.append(j)
            i += 1
            j += 1
        elif (A[i] < B[j]):
            i += 1
        elif (A[i] > B[j]):
            j += 1
    if (i < len(A)):
        while(j < len(B)):
            if (A[i] == B[j]):
                aligned_A.append(i)
                aligned_B.append(j)
            j += 1
    if (j < len(B)):
        while(i < len(A)):
            if (A[i] == B[j]):
                aligned_A.append(i)
                aligned_B.append(j)
            i += 1
    return aligned_A, aligned_B

def _find_join_set_then_match(A, B, F_A, F_B):
    i = 0
    j = 0
    match_list = [0] * len(A)
    while (i < len(A) and j < len(B)):
        if (A[i] == B[j]):
            if (F_A[i] == F_B[j]):
                match_list[i] = 1
            i += 1
            j += 1
        elif (A[i] < B[j]):
            i += 1
        elif (A[i] > B[j]):
            j += 1
    if (i < len(A)):
        while(j < len(B)):
            if (A[i] == B[j] and F_A[i] == F_B[j]):
                match_list[i] = 1
            j += 1
    if (j < len(B)):
        while(i < len(A)):
            if (A[i] == B[j] and F_A[i] == F_B[j]):
                match_list[i] = 1
            i += 1
    return match_list