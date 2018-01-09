from music21 import note
from music21 import stream
import random 

#d = {0:'C4',
#     1:'C#4',
#     2:'D4',
#     3:'D#4',
#     4:'E4', 
#     5:'F4', 
#     6:'F#4', 
#     7:'G4',
#     8:'G#4',
#     9:'A4',
#    10:'A#4',
#    11:'B4',
#    12:'C5'}  

d = {0:'C4',
     1:'D4',
     2:'E4',
     3:'F4',
     4:'G4', 
     5:'A4', 
     6:'B4', 
     7:'C5'}
for j in range(10): 
    s1 = stream.Stream()
    s1.append(note.Rest())
    s1.append(note.Rest())
    s1.append(note.Rest())
    s1.append(note.Rest())
    for i in range(1004):
        r = random.randint(1,7)
        n = d[r]
        s1.append(note.Note(d[r],type = 'quarter'))

   
    s1.write()    
        