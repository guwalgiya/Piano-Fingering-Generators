# ===============================================
# Import Packages and Functions
import music21.converter     as converter
import tkinter.filedialog    as filedialog
import music21.articulations as articulations
import tkinter


# ===============================================
# Main Function
def labelFingerings():   

    # =============================================== 
    root  = tkinter.Tk() 
    

    # =============================================== 
    # Remove the window
    root.withdraw()


    # =============================================== 
    # Program asks users to open a file
    path  = filedialog.askopenfilename()
    piece = converter.parse(path)


    # ===============================================
    # Program asks users to enter a serie of numbers
    input_fingering = input("Please Enter the fingerings for right hand ")
    input_fingering = input_fingering.replace(" ", "")
    

    # ===============================================
    # Program adds fingerings to the chosen piece
    piece = add_fingers(piece, input_fingering)
    

    # ===============================================
    # Program overwrites the old file with new fingerings
    piece.write("xml", fp = path)
 

# ===============================================
def add_fingers(piece, input_fingering):


	# ===============================================
	# i : index of component of a piece
    remained_fingering = input_fingering
    for i in range(len(piece)):

        
    	# ===============================================
        try:

            
        	# ===============================================
        	# j : measure index in a component (right hand or left hand)
            for j in range(len(piece[i])):
                if str(type(piece[i][j])) == "<class 'music21.stream.Measure'>":


                	# ===============================================
                    cur_measure        = piece[i][j]
                    num_fingers_used   = addMeasureFingering(i, j, piece, cur_measure, remained_fingering)
                    remained_fingering = remained_fingering[num_fingers_used :]
            

            # ===============================================
            break


        # ===============================================    
        except:
            pass
    

    # ===============================================    
    return piece


# ===============================================   
def addMeasureFingering(i, j, piece, measure, remained_fingering):
    

    # k : index in a measure, note or chord
    num_fingers_used = 0  


    # ===============================================    
    # k : index in a measure, note or chord
    for k in range(len(measure)):


    	# ===============================================    
        # k : work on a note
        if str(type(measure[k]))         == "<class 'music21.note.Note'>":
            cur_finger                   =  remained_fingering[num_fingers_used]
            num_fingers_used             += 1
            piece[i][j][k].articulations =  [articulations.Fingering(int(cur_finger))]
            
        

        # ===============================================    
        # k : work on a chord
        elif str(type(measure[k])) == "<class 'music21.chord.Chord'>":
            chord_size             =  piece[i][j][k].multisetCardinality
            chord_fingering        =  remained_fingering[num_fingers_used : num_fingers_used + chord_size]
            num_fingers_used       += chord_size  
            

            # ===============================================    
            # Add finger for every note in the chord
            for cur_finger in chord_fingering:
                piece[i][j][k].articulations.append(articulations.Fingering(int(cur_finger)))
    

    # ===============================================            
    return num_fingers_used


# ===============================================
labelFingerings()