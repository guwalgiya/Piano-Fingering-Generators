from music21 import *
from tkinter import *
import string
import random

def main():

    RHF = input('Input Right Hand Fingering \n')
    LHF = input('Input Left Hand Fingering \n')
    
    RHF = RHF.replace(' ','')
    LHF = LHF.replace(' ','')
    for i in range(len(piece)):
        try:            
            Hand(i,piece[i],RHF)
            index = i + 1
            break
        except:
            pass
        
    for i in range(len(piece)):
        try:
            Hand(index + i,piece[index + i],LHF)
            break
        except:
            pass
    
def Hand(i, hand, fingerset):       
    for j in range(len(hand)):
        if str(type(hand[j])) == "<class 'music21.stream.Measure'>":
            measure = hand[j]
            numberOfFingers = change(i,measure,j,fingerset)
            fingerset = fingerset[numberOfFingers:]

    
def change(i,measure,j,fingerset):
    x = 0 #x is counting the number of fingers used in this measure
    for k in range(len(measure)):
        if str(type(measure[k])) == "<class 'music21.note.Note'>":
            finger = fingerset[x]
            piece[i][j][k].articulations = [articulations.Fingering(int(finger))]
            x = x + 1
            
        elif str(type(measure[k])) == "<class 'music21.chord.Chord'>":
            size = piece[i][j][k].multisetCardinality
            fingersubset = fingerset[x:x + size]
            for finger in fingersubset:
                piece[i][j][k].articulations.append(articulations.Fingering(int(finger)))
            x = x + size   
    return x   

path = filedialog.askopenfilename()
piece = converter.parse(path)
main()
piece.show()
