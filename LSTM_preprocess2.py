import os
import glob
from music21 import converter

import xml_to_midi
import split_by_chord

def main(training_path):
    book_interval = []
    book_finger = []
    
    #go to the path where the training set locates
    os.chdir(training_path)
    
    #have to parse '.xml' files
    for file_name in glob.glob("*.xml"):  
        song_interval, song_finger = preprocess(file_name)     
        book_interval = book_interval + song_interval
        book_finger = book_finger + song_finger
        
    return book_interval, book_finger

def preprocess(file_name):
    print(file_name)
    song_interval = []
    song_finger = []
    
    piece = converter.parse(file_name)
    
    # change this piece's right hand part into midi
    midi_list = xml_to_midi.main(piece)
    song_interval, song_finger = split_by_chord.main(midi_list)
    
    return song_interval, song_finger