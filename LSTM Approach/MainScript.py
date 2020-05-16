from Utils import shuffleDataset, SplitJPData, saveToPickle, loadFromPickle, SplitChopinData, SplitMozartData, SplitBachData
from JPDataPreProcessing import toVectorTrainFormat, toVectorTestFormat, toInterleavedTrainFormat, toVectorFutureTrainFormat
from TrainModel import trainModel
from TestVectorModel import loadModel, testVecModelSave, testVecModelEval, testVecFutureModelSave
from EvaluateJPMethod import evaluate_yz, evaluate_jp, evaluate_yz_single
import statistics
from JPDataPreProcessing import getListsFromSingeFile
import numpy as np

DATA_DIR = '../Datasets/JPDataset/'
HMM_RES_DIR = '../Datasets/JPResDataset/'
# HMM_RES_DIR = '../Datasets/JPESTResults/selfTrained/FHMM1/'
# # prepare raw training set and testing set
# SPLIT_RATIO = 0.75 # ratio of train data
# train_files, test_files = shuffleDataset(SPLIT_RATIO, DATA_DIR)
# saveToPickle(train_files, '../Datasets/processed/train_filenames.pkl')
# saveToPickle(test_files, '../Datasets/processed/test_filenames.pkl')
# train_files, test_files, hmm_res_files = SplitJPData(DATA_DIR, HMM_RES_DIR)
train_files, test_files, hmm_res_files = SplitChopinData(DATA_DIR)
# train_files, test_files, hmm_res_files = SplitMozartData(DATA_DIR)
# train_files, test_files, hmm_res_files = SplitBachData(DATA_DIR)
# print(hmm_res_files)
# saveToPickle(train_files, 'train_filenames.pkl')
# saveToPickle(test_files, 'hmm_res_files.pkl')

# Training related
# print('loading train filenames')
# train_files = loadFromPickle('../Datasets/processed/train_filenames.pkl')
# print('preprocessing raw train data')
# train_input_list, train_label_list = toInterleavedTrainFormat(train_files, DATA_DIR)
train_input_list, train_label_list = toVectorFutureTrainFormat(train_files, DATA_DIR)
# print(len(train_label_list))
# train_input_list, train_label_list = toVectorTrainFormat(train_files, DATA_DIR)
# TRAIN_INPUT_PATH = '../Datasets/processed/train_input_list_4_vector.pkl'
# TRAIN_LABEL_PATH = '../Datasets/processed/train_label_list_4_vector.pkl'
# saveToPickle(train_input_list, TRAIN_INPUT_PATH)
# saveToPickle(train_label_list, TRAIN_LABEL_PATH)
# Train the network
trainModel(train_input_list, train_label_list, num_epochs=8, batch_size=8)

# ## Testing related
# # print('loading train filenames')
# # test_files = loadFromPickle('../Datasets/processed/test_filenames.pkl')
# print('preprocessing raw test data')
# # TEST_INPUT_PATH = '../Datasets/processed/test_input_list_4_vector.pkl'
# # TEST_LABEL_PATH = '../Datasets/processed/test_label_list_4_vector.pkl'
test_input_list, test_label_list, _ = toVectorTestFormat(test_files, DATA_DIR)
# # saveToPickle(test_input_list, TEST_INPUT_PATH)
# # saveToPickle(test_label_list, TEST_LABEL_PATH)
# # Test the network
# model = loadModel()
# for test_file in test_files:
#     test_input_list, test_label_list, _ = toVectorTestFormat([test_file], DATA_DIR)
#     vec_fingering_res = testVecFutureModelSave(test_input_list, test_label_list, model)
#     evaluate_yz_single(test_file, DATA_DIR, vec_fingering_res)

# model = loadModel()

# test_input_list, test_label_list, _ = toVectorTestFormat(['009-1_fingering.csv'], DATA_DIR)
# finger_res = testVecModelSave(test_input_list, test_label_list, model)
# note_list, _, _, _, id_list = getListsFromSingeFile('009-1_fingering.csv', DATA_DIR)

# np_id = np.array(id_list)
# np_note = np.array(note_list)
# np_finger = np.array(finger_res)
# np_out = np.vstack((np_id, np_note))
# np_out = np.vstack((np_out, np_finger))
# print(np_out.T)
# evaluate_yz(hmm_res_files, DATA_DIR, HMM_RES_DIR)

# Multiple fingering for one piece evaluation
model = loadModel()
# group muli fingering files
file_dict = {}
for test_file in test_files:
    pre_fix = test_file.split('-')[0]
    if pre_fix in file_dict:
        file_dict[pre_fix].append(test_file)
    else:
        temp_list = [test_file]
        file_dict[pre_fix] = temp_list

M_gen_list = [] 
M_high_list = [] 
M_soft_list = []
for hmm_res_file in hmm_res_files:
    pre_fix = hmm_res_file.split('-')[0]
    if pre_fix in file_dict:
        multi_files = file_dict[pre_fix]
        test_input_list, test_label_list, test_id_list = toVectorTestFormat([hmm_res_file], HMM_RES_DIR)
        vec_fingering_res = testVecFutureModelSave(test_input_list, test_label_list, model)
        M_gen, M_high, M_soft = evaluate_jp(multi_files, DATA_DIR, vec_fingering_res, test_id_list[0])
        M_gen_list.append(M_gen)
        M_high_list.append(M_high)
        M_soft_list.append(M_soft)
        # print(hmm_res_file)
        # print('M_GEN: ', M_gen)
        # print('M_HIGH: ', M_high)
        # print('M_SOFT: ', M_soft)
print('Total mean: ')
print('M_GEN: ', statistics.mean(M_gen_list))
print('M_HIGH: ', statistics.mean(M_high_list))
print('M_SOFT: ', statistics.mean(M_soft_list))


# below are used to test JP Hmm results

# Evaluate JP hmm method with same test_files
# abs_true, proper, abs_wrong = evaluate_yz(hmm_res_files, DATA_DIR, HMM_RES_DIR)
# print(f'abs_true: {abs_true}, proper: {proper}, abs_wrong: {abs_wrong}')

# file_dict = {}
# for test_file in test_files:
#     pre_fix = test_file.split('-')[0]
#     if pre_fix in file_dict:
#         file_dict[pre_fix].append(test_file)
#     else:
#         temp_list = [test_file]
#         file_dict[pre_fix] = temp_list

# M_gen_list = [] 
# M_high_list = [] 
# M_soft_list = []
# for hmm_res_file in hmm_res_files:
#     pre_fix = hmm_res_file.split('-')[0]
#     if pre_fix in file_dict:
#         multi_files = file_dict[pre_fix]
#         note_list, finger_list, interval_list, accidental_list, id_list = getListsFromSingeFile(hmm_res_file, HMM_RES_DIR)
#         M_gen, M_high, M_soft = evaluate_jp(multi_files, DATA_DIR, finger_list, id_list)
#         M_gen_list.append(M_gen)
#         M_high_list.append(M_high)
#         M_soft_list.append(M_soft)
#         # print(hmm_res_file)
#         # print('M_GEN: ', M_gen)
#         # print('M_HIGH: ', M_high)
#         # print('M_SOFT: ', M_soft)
# print('Total mean: ')
# print('M_GEN: ', statistics.mean(M_gen_list))
# print('M_HIGH: ', statistics.mean(M_high_list))
# print('M_SOFT: ', statistics.mean(M_soft_list))

