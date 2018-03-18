import music21.converter     as converter
import music21.articulations as articulations
import tkinter.filedialog    as filedialog
import tkinter

def main():    
    # Program asks users to open a file
    root          = tkinter.Tk()
    root.withdraw()
    path          = filedialog.askopenfilename()
    piece         = converter.parse(path) 
    
    # Program asks users to enter a serie of numbers
    input_fingers = input("Please Enter the fingerings for right hand ")
    input_fingers = input_fingers.replace(" ", "")
    
    # Program adds fingerings to the chosen piece
    piece         = add_fingers(piece, input_fingers)
    
    # Program overwrites the old file with new fingerings
    piece.write('xml', fp = path)
    
def add_fingers(piece, input_fingers):
    remained_fingers                     =   input_fingers
    for i in range(len(piece)):
        try:
            for j in range(len(piece[i])):
                if str(type(piece[i][j])) == "<class 'music21.stream.Measure'>":
                    measure               =   piece[i][j]
                    num_fingers_used      =   measure_finger(i, j, piece, measure, remained_fingers)
                    remained_fingers      =   remained_fingers[num_fingers_used:]
            break
        except:
            pass
           
    return piece

def measure_finger(i, j, piece, measure, remained_fingers):
    num_fingers_used                     =  0  
    for k in range(len(measure)):
        if str(type(measure[k]))         == "<class 'music21.note.Note'>":
            finger                       =  remained_fingers[num_fingers_used]
            piece[i][j][k].articulations =  [articulations.Fingering(int(finger))]
            num_fingers_used             += 1

        elif str(type(measure[k]))       == "<class 'music21.chord.Chord'>":
            chord_size                   =  piece[i][j][k].multisetCardinality
            chord_finger                 =  remained_fingers[num_fingers_used : num_fingers_used + chord_size]
            num_fingers_used             += chord_size  
            
            for finger in chord_finger:
                piece[i][j][k].articulations.append(articulations.Fingering(int(finger)))
                
    return num_fingers_used

main()