def main(book_interval, book_finger):
    book_interval = remove_interval_greater_than_12(book_interval)
    
    input_list = []
    label_list = []
    for i in range(len(book_interval)):
        seq_input_list, seq_label_list = create_training(book_interval[i], book_finger[i])
        print('%%%%%%%%%%%%%%%%%%%%%')
        print(book_interval[i])
        print(seq_input_list)
        print(seq_label_list)
        input_list = input_list + seq_input_list
        label_list = label_list + seq_label_list
        
    return input_list, label_list    

def create_training(seq_interval, seq_finger):
    seq_input = []
    seq_label = []
    
    for i in range(len(seq_interval) - 3):
        
        seq_label.append(seq_finger[i + 3])
        
        a = seq_finger[i]
        b = seq_interval[i]
        c = seq_finger[i + 1]
        d = seq_interval[i + 1] 
        e = seq_finger[i + 2]
        f = seq_interval[i + 2]
        seq_input.append([a,b,c,d,e,f])
        
    return seq_input, seq_label

def remove_interval_greater_than_12(book_interval):
    for item in book_interval:
        for i in range(len(item)):
            if item[i] < -12:
                item[i] = -12
            elif item[i] > 12:
                item[i] = 12
    return book_interval
