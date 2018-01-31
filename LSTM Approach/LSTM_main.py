import tkinter
from tkinter import filedialog

import LSTM_preprocess
import LSTM_preprocess2
import LSTM_2to1Preprocessing
import LSTM_3to1Preprocessing
import LSTM_4to1Preprocessing
import LSTM_6to1Preprocessing
import LSTM_8to1Preprocessing
# Ask where the trianing set locates(need a folder)
root = tkinter.Tk()
root.withdraw()
training_path = filedialog.askdirectory()

# preprocess: make the trianing set into monotonic sequences
#book_interval_up, book_finger_up, book_interval_down, book_finger_down = LSTM_preprocess.main(training_path)

# preprocess2: split the trianing set based on chords location
print('Start to Parsing Data')
book_interval, book_finger = LSTM_preprocess2.main(training_path)

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Start to create training sequences')
input_list, label_list = LSTM_8to1Preprocessing.main(book_interval, book_finger)
print('Ready to train the model !!')