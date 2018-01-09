from music21 import *
from tkinter import filedialog
import tkinter
import string
import random



def main():
    for j in range(len(piece[1])):
        try:
            if str(type(piece[1][j])) == "<class 'music21.stream.Measure'>":
               
                    change(piece[1][j],j)
        except:
            pass
            
        j = j + 1
    print('so far so good')     
    
def change(measure,j):
    k = 0
    print('measure')
    for k in range(len(measure)):
        try:
            if str(type(measure[k])) == "<class 'music21.note.Note'>":
                #finger = random.randint(1,5)
                finger = fingers[0]
                fingers =fingers[1:]
                piece[1][j][k].articulations = [articulations.Fingering(finger)]

                print(piece[1][j][k].articulations)
        except:
            pass
        
root = tkinter.Tk()
root.withdraw()
path = filedialog.askopenfilename()
piece = converter.parse(path)

main()

print('right here')
piece.write()
print('Done')


