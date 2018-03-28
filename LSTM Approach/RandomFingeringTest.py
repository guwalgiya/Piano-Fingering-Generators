import pickle
import EvaluatePhrase
import random
def main(num_round):
    input_list    = pickle.load(open("../Datasets/processed/test_input_list.pkl", "rb"))
    label_list    = pickle.load(open("../Datasets/processed/test_label_list.pkl", "rb"))
    
    total_acc           = 0
    total_wrong_rate    = 0
    total_improper_rate = 0
    for i in range(num_round):
        acc, wrong_rate, improper_rate  = random_fingering(input_list, label_list)
        total_acc                       = acc           + total_acc
        total_wrong_rate                = wrong_rate    + total_wrong_rate
        total_improper_rate             = improper_rate + total_improper_rate
        if (i + 1) % 1000 == 0:
            print("Round ", i + 1, (len(str(num_round)) - len(str(i + 1))) * ' ',"average acc is", total_acc / (i + 1), "average wrong rate is", total_wrong_rate / (i+1), "average improper rate is", total_improper_rate / (i+1))

def random_fingering(input_list, label_list):
    test_set_abs_true  = 0
    test_set_abs_false = 0
    test_set_improper  = 0
    for i in range(len(input_list)):
        
        random_f = []
        for j in range(len(label_list[i])): 
            random_f.append(random.randint(1,5))
        phrase_abs_true, phrase_abs_false, phrase_improper = EvaluatePhrase.main(input_list[i], random_f, label_list[i])
        test_set_abs_true  = test_set_abs_true  + phrase_abs_true
        test_set_abs_false = test_set_abs_false + phrase_abs_false
        test_set_improper  = test_set_improper  + phrase_improper
    return test_set_abs_true / sum(len(phrase) for phrase in (label_list)), test_set_abs_false / sum(len(phrase) for phrase in (input_list)), test_set_improper / sum(len(phrase) for phrase in (input_list))
main(10000)