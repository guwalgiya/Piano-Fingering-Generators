import GetBlockedData
import pickle
from parameters import BLOCK_LENGTH
normalization          = False
training_path          = '../Datasets/Complete_Training_Dataset'
testing_path           = '../Datasets/Complete_Testing_Dataset'

#train_input_list, train_label_list = GetBlockedData.main(training_path, BLOCK_LENGTH, True, normalization)
test_input_list, test_label_list = GetBlockedData.main(testing_path, BLOCK_LENGTH, False, normalization)
if normalization:
    #train_label_list             = [int(x * 5) for x in train_label_list]
    test_label_list              = [int(x * 5) for x in test_label_list]
#pickle.dump(train_input_list, open('../Datasets/processed/train_input_list_4_bi.pkl', 'wb'))
#pickle.dump(train_label_list, open('../Datasets/processed/train_label_list_4_bi.pkl', 'wb'))
pickle.dump(test_input_list, open('../Datasets/processed/test_input_list.pkl', 'wb'))
pickle.dump(test_label_list, open('../Datasets/processed/test_label_list.pkl', 'wb'))
