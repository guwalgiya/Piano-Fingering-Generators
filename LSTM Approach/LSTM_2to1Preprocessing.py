
def main(book_interval, book_finger):
    book_interval = remove_interval_greater_than_12(book_interval)
    
    input_list = []
    label_list = []
    for i in range(len(book_interval)):
        seq_input_list, seq_label_list = create_training(book_interval[i], book_finger[i])
        input_list = input_list + seq_input_list
        label_list = label_list + seq_label_list
        
    return input_list, label_list
        
# Terminology
# 1 -125
# 1 - 25: finger 1
# 26 - 50: finger 2
# 51 - 75: finger 3
# 76 - 100: finger 4
# 101 - 125: finger 5
def create_training(seq_interval, seq_finger):
    seq_input = []
    seq_label = []
    
    for i in range(len(seq_interval) - 2):
        seq_label.append(seq_finger[i + 2])
        
        a = terminology(seq_finger[i], seq_interval[i])
        b = terminology(seq_finger[i+1],seq_interval[i+1])
        seq_input.append([a,b])
        
    return seq_input, seq_label

def terminology(finger, interval):
    return (finger - 1) * 25 + (interval + 13) 


def remove_interval_greater_than_12(book_interval):
    for item in book_interval:
        for i in range(len(item)):
            if item[i] < -12:
                item[i] = -12
            elif item[i] > 12:
                item[i] = 12
    return book_interval