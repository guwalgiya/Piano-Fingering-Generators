from music21 import *

def main(piece):
    for i in range(len(piece)):
        
        # to test if this is music, not title or author or something else
        if str(type(piece[i])) == "<class 'music21.stream.Part'>":   
            
            # now we find rightHand,which is piece[i]
            hand_midi = measure_finder(piece[i])
            break
    
    #So far hand_midi is the right_hand_midi list, NOT BOTH HANDSSSSS!!!
    return hand_midi

#used in tomidi(), righthand = everything for the right hand
def measure_finder(hand):
    hand_midi = []
    
    for i in range(len(hand)):
        
        #to test if this is a measure
        if str(type(hand[i])) == "<class 'music21.stream.Measure'>": 
            
            # hand[j] is a measure
            measure_midi = inside_measure(hand[i])    
            
            hand_midi = hand_midi + measure_midi   
    
    return hand_midi        
        

def inside_measure(measure): #used in measurefinder, measure = the measure we are working on now.
    measure_midi= []
    
    #count the elements in a measure, could be a note or a chord
    for i in range(len(measure)): 
        
        #if this element is a note
        if str(type(measure[i])) == "<class 'music21.note.Note'>": 
            measure_midi.append((measure[i].pitch.midi,int(str(measure[i].articulations[0])[-2])))
            
        #if this element is a chord
        elif str(type(measure[i])) == "<class 'music21.chord.Chord'>": 
            chordlist              = []
            
            #p = part
            for p in measure[i]:    
                chordlist.append(p.pitch.midi)     #chordlist is the sub-list reprents a chord
            
            #put the sublist into the midilist of this measure
            measure_midi.append([chordlist,6]) 
            
    return measure_midi