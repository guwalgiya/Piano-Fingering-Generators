import glob
import music21.converter as converter

import xml_to_midi
import split_by_chord

def main(training_path, train=True, normalization=True):
    book_interval = []
    book_finger   = []
    #go to the path where the training set locates
    # chdir(training_path)
    #have to parse '.xml' files
    for file_name in glob.glob(training_path + "/*.xml"):
        # song_interval is a 2d array, each row is seperated by chord
        song_interval, song_finger = preprocess(file_name, normalization)
        if train:
            book_interval              = book_interval + song_interval
            book_finger                = book_finger   + song_finger
        else:
            book_interval.append(song_interval)
            book_finger.append(song_finger)
    return book_interval, book_finger

def preprocess(file_name, normalization=True):
    print('preprocessing: '+ file_name)
    piece_interval = []
    piece_finger   = []   
    piece          = converter.parse(file_name)
    
    # change this piece's right hand part into midi
    midi_list                    = xml_to_midi.main(piece)
    piece_interval, piece_finger = split_by_chord.main(midi_list, normalization)
    
    return  piece_interval, piece_finger