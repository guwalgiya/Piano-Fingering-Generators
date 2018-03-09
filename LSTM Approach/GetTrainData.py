import DataPreprocess
def main(training_path, block_length):
    book_interval, book_finger = DataPreprocess.main(training_path)
    book_interval = remove_interval_greater_than_12(book_interval)
    input_list = []
    label_list = []
    for i in range(len(book_interval)):
        seq_input_list, seq_label_list = block_sequence(book_interval[i], book_finger[i], block_length)
        input_list += seq_input_list
        label_list += seq_label_list
    return input_list, label_list

def block_sequence(seq_interval, seq_finger, block_length):
    seq_input = []
    seq_label = []
    for i in range(len(seq_interval) - (block_length-1)):
        seq_label.append(seq_finger[i + block_length])
        temp_block = []
        for j in xrange(block_length):
            temp_block.append(seq_finger[i+j])
            temp_block.append(seq_interval[i+j])
        seq_input.append(temp_block)
    return seq_input, seq_label

def remove_interval_greater_than_12(book_interval):
    for item in book_interval:
        for i in range(len(item)):
            if item[i] < -12:
                item[i] = -12
            elif item[i] > 12:
                item[i] = 12
    return book_interval
