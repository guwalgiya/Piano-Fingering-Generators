import GetTrainData
import pickle
block_length           = 4
normalization          = False
training_path          = '../Datasets/Complete_Training_Dataset'
testing_path           = '../Datasets/Complete_Testing_Dataset'

train_input_list, train_label_list = GetTrainData.main(testing_path, block_length, True, normalization)
test_input_list, test_label_list = GetTrainData.main(testing_path, block_length, False, normalization)
# train_label_list             = [int(x * 5) for x in train_label_list]
test_input_list = [seq[block_length-1:] for seq in test_input_list]
test_label_list = [seq[block_length-1:] for seq in test_label_list]
for item in test_input_list:
    print(item)
for item in test_label_list:
    print(item)
print("----------------------------------")

# test_label_list              = [int(x * 5) for x in test_label_list]
# pickle.dump(train_input_list, open('../Datasets/processed/train_input_list.pkl', 'wb'))
# pickle.dump(train_label_list, open('../Datasets/processed/train_label_list.pkl', 'wb'))
# pickle.dump(test_input_list, open('../Datasets/processed/test_input_list.pkl', 'wb'))
# pickle.dump(test_input_list, open('../Datasets/processed/test_input_list.pkl', 'wb'))
