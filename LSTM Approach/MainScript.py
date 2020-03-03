from Utils import shuffleDataset, saveToPickle, loadFromPickle
from JPDataPreProcessing import toVectorTrainFormat, toVectorTestFormat, toInterleavedTrainFormat
from TrainModel import trainModel
from TestVectorModel import loadModel, testVecModel
from EvaluateJPMethod import evaluate

DATA_DIR = '../Datasets/JPDataset/'
# # prepare raw training set and testing set
# SPLIT_RATIO = 0.75 # ratio of train data
# train_files, test_files = shuffleDataset(SPLIT_RATIO, DATA_DIR)
# saveToPickle(train_files, '../Datasets/processed/train_filenames.pkl')
# saveToPickle(test_files, '../Datasets/processed/test_filenames.pkl')
# use previosly splited train/test set

## Training related
print('loading train filenames')
train_files = loadFromPickle('../Datasets/processed/train_filenames.pkl')
print('preprocessing raw train data')
# train_input_list, train_label_list = toInterleavedTrainFormat(train_files, DATA_DIR)
TRAIN_INPUT_PATH = '../Datasets/processed/train_input_list_4_vector.pkl'
TRAIN_LABEL_PATH = '../Datasets/processed/train_label_list_4_vector.pkl'
train_input_list, train_label_list = toVectorTrainFormat(train_files, DATA_DIR)
saveToPickle(train_input_list, TRAIN_INPUT_PATH)
saveToPickle(train_label_list, TRAIN_LABEL_PATH)
# Train the network
trainModel(train_input_list, train_label_list, num_epochs=40, batch_size=20)

## Testing related
print('loading train filenames')
test_files = loadFromPickle('../Datasets/processed/test_filenames.pkl')
print('preprocessing raw test data')
TEST_INPUT_PATH = '../Datasets/processed/test_input_list_4_vector.pkl'
TEST_LABEL_PATH = '../Datasets/processed/test_label_list_4_vector.pkl'
test_input_list, test_label_list = toVectorTestFormat(test_files, DATA_DIR)
saveToPickle(test_input_list, TEST_INPUT_PATH)
saveToPickle(test_label_list, TEST_LABEL_PATH)
# Test the network
model = loadModel()
testVecModel(test_input_list, test_label_list, model)
# Evaluate JP hmm method with same test_files
evaluate(test_files, DATA_DIR, '../Datasets/JPESTResults/selfTrained/FHMM2/')

