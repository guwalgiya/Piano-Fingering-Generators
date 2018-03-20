import DataPreprocess
def main(file_path, block_length, train=True, normalizaiton=True):
    input_list = []
    label_list = [] 
    if train:
        book_interval, book_finger = DataPreprocess.main(file_path, True, normalizaiton)
        book_interval = remove_interval_greater_than_12(book_interval)
        for i in range(len(book_interval)):
            seq_input_list, seq_label_list = block_sequence(book_interval[i], book_finger[i], block_length)
            input_list += seq_input_list
            label_list += seq_label_list
    else:
        book_interval, book_finger = DataPreprocess.main(file_path, False, normalizaiton)
        for song_interval in book_interval:
            remove_interval_greater_than_12(song_interval)
        for i in range(len(book_interval)):
            # temp_input_list = []
            # temp_label_list = []
            # for j in range(len(book_interval[i])):
            #     seq_input_list, seq_label_list = block_sequence(book_interval[i][j], book_finger[i][j], block_length)
            #     temp_input_list += seq_input_list
            #     temp_label_list += seq_label_list
            # input_list.append(temp_input_list)
            # label_list.append(temp_label_list)
            temp_input_list = []
            temp_label_list = []
            for j in range(len(book_interval[i])):
                temp_input_list += book_interval[i][j]
                temp_label_list += book_finger[i][j]
            input_list.append(temp_input_list)
            label_list.append(temp_label_list)
    return input_list, label_list

def block_sequence(seq_interval, seq_finger, block_length, train=True):
    seq_input = []
    seq_label = []
    for i in range(len(seq_interval) - (block_length - 1)):
        seq_label.append(seq_finger[i + block_length])
        temp_block = []
        for j in range(block_length):
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
