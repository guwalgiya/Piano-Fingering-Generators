import os
import glob
from music21 import converter

import xml_to_midi
import midi_divider
import sequence_work

# Training
# We want to train our model, we need load all the trianing files.
# @Interval_list
# @Finger_list
def main(training_path):
    book_interval_up = []
    book_finger_up = []
    book_interval_down = []
    book_finger_down = []
    
    #go to the path where the training set locates
    os.chdir(training_path)
    
    #have to parse '.xml' files
    for file_name in glob.glob("*.xml"):        
        song_interval_up, song_finger_up, song_interval_down, song_finger_down = preprocess(file_name)
        
        book_interval_up = book_interval_up + song_interval_up
        book_finger_up = book_finger_up + song_finger_up
        book_interval_down = book_interval_down + song_interval_down
        book_finger_down = book_finger_down + song_finger_down
        
        
    return book_interval_up, book_finger_up, book_interval_down, book_finger_down 


def preprocess(file_name):
    print(file_name)
    
    song_interval_up = []
    song_finger_up = []
    song_interval_down = []
    song_finger_down = []
    
    # analyze a piece
    piece = converter.parse(file_name)
    
    # change this piece's right hand part into midi
    midi_list = xml_to_midi.main(piece)
    
    # divide midi into monotonic list
    midi_list_monotonic = midi_divider.main(midi_list)
        
    for i in range(len(midi_list_monotonic)):
                
        sequence = sequence_work.chord_filter(midi_list_monotonic[i])
        
        seq_interval_up,seq_finger_up,seq_interval_down,seq_finger_down = sequence_work.analysis(sequence)
        
        # sum up for the song
        song_interval_up = song_interval_up + seq_interval_up
        song_finger_up = song_finger_up + seq_finger_up
        song_interval_down = song_interval_down + seq_interval_down
        song_finger_down = song_finger_down + seq_finger_down
        
    return song_interval_up, song_finger_up, song_interval_down, song_finger_down
    
    
