from Utils import shuffleDataset, SplitJPData, saveToPickle, loadFromPickle
from JPDataPreProcessing import toVectorTrainFormat, toVectorTestFormat, toInterleavedTrainFormat
from TrainModel import trainModel
from TestVectorModel import loadModel, testVecModelSave, testVecModelEval
from EvaluateJPMethod import evaluate_yz, evaluate_jp
import statistics

DATA_DIR = '../Datasets/JPDataset/'
HMM_RES_DIR = '../Datasets/JPResDataset/'
# # prepare raw training set and testing set
# SPLIT_RATIO = 0.75 # ratio of train data
# train_files, test_files = shuffleDataset(SPLIT_RATIO, DATA_DIR)
# saveToPickle(train_files, '../Datasets/processed/train_filenames.pkl')
# saveToPickle(test_files, '../Datasets/processed/test_filenames.pkl')
train_files, test_files, hmm_res_files = SplitJPData(DATA_DIR, HMM_RES_DIR)

# Training related
# print('loading train filenames')
# train_files = loadFromPickle('../Datasets/processed/train_filenames.pkl')
print('preprocessing raw train data')
# train_input_list, train_label_list = toInterleavedTrainFormat(train_files, DATA_DIR)
train_input_list, train_label_list = toVectorTrainFormat(train_files, DATA_DIR)
# TRAIN_INPUT_PATH = '../Datasets/processed/train_input_list_4_vector.pkl'
# TRAIN_LABEL_PATH = '../Datasets/processed/train_label_list_4_vector.pkl'
# saveToPickle(train_input_list, TRAIN_INPUT_PATH)
# saveToPickle(train_label_list, TRAIN_LABEL_PATH)
# Train the network
trainModel(train_input_list, train_label_list, num_epochs=10, batch_size=20)

# ## Testing related
# print('loading train filenames')
# # test_files = loadFromPickle('../Datasets/processed/test_filenames.pkl')
# print('preprocessing raw test data')
# # TEST_INPUT_PATH = '../Datasets/processed/test_input_list_4_vector.pkl'
# # TEST_LABEL_PATH = '../Datasets/processed/test_label_list_4_vector.pkl'
test_input_list, test_label_list, _ = toVectorTestFormat(hmm_res_files, DATA_DIR)
# # saveToPickle(test_input_list, TEST_INPUT_PATH)
# # saveToPickle(test_label_list, TEST_LABEL_PATH)
# # Test the network
model = loadModel()
testVecModelEval(test_input_list, test_label_list, model, verbose=True)

# Evaluate JP hmm method with same test_files
# evaluate_yz(test_files, DATA_DIR, '../Datasets/JPESTResults/selfTrained/FHMM2/')
# evaluate_yz(hmm_res_files, DATA_DIR, HMM_RES_DIR)

# # Multiple fingering for one piece evaluation
# model = loadModel()
# # group muli fingering files
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
#     multi_files = file_dict[pre_fix]
#     test_input_list, test_label_list, test_id_list = toVectorTestFormat([hmm_res_file], HMM_RES_DIR)
#     vec_fingering_res = testVecModelSave(test_input_list, test_label_list, model)
#     M_gen, M_high, M_soft = evaluate_jp(file_dict[pre_fix], DATA_DIR, vec_fingering_res, test_id_list[0])
#     M_gen_list.append(M_gen)
#     M_high_list.append(M_high)
#     M_soft_list.append(M_soft)

# print('M_GEN: ', statistics.mean(M_gen_list))
# print('M_HIGH: ', statistics.mean(M_high_list))
# print('M_SOFT: ', statistics.mean(M_soft_list))

