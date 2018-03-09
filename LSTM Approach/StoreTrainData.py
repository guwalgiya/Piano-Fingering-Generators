import GetTrainData
import pickle
block_length = 4
training_path = '../Datasets/Czerny_599_with_Fingering'
input_list, label_list = GetTrainData.main(training_path, block_length)
pickle.dump(input_list, open('../Datasets/processed/input_list.pkl', 'wb'))
pickle.dump(label_list, open('../Datasets/processed/label_list.pkl', 'wb'))