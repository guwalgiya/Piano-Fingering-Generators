import pickle
import EvaluatePhrase
import random
def main(num_round):
    input_list    = pickle.load(open("../Datasets/processed/test_input_list.pkl", "rb"))
    label_list    = pickle.load(open("../Datasets/processed/test_label_list.pkl", "rb"))
    
    total_acc     = 0
    for i in range(num_round):
        acc       = random_fingering(input_list, label_list)
        total_acc = acc + total_acc
        print("Round ", i + 1, (len(str(num_round)) - len(str(i + 1))) * ' ',"average acc is", total_acc / (i + 1), "acc is", acc)

def random_fingering(input_list, label_list):
    test_set_abs_true = 0
    for i in range(len(input_list)):
        
        random_f = []
        for j in range(len(label_list[i])): 
            random_f.append(random.randint(1,5))
        phrase_abs_true, _, _ = EvaluatePhrase.main(input_list[i], label_list[i], random_f)
        test_set_abs_true = test_set_abs_true + phrase_abs_true
    
    return test_set_abs_true / sum(len(phrase) for phrase in (label_list))
main(10000)