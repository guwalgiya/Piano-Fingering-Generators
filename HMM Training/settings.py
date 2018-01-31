import tkinter
from tkinter import filedialog
from music21 import *

#此方法用于初始化
def initial():
    
    #Method1:Program asks users to open a file
    root = tkinter.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    
    #Method2: Type in the file we want to analyze
    #path = "C:/Users/GuwalgiyaGuan/Documents/2000.Music Technology Master/7100.Piano Fingering/Codes/Test5.xml"

    #piece is the piano music we are working on
    global piece  
    piece = converter.parse(path)
    
    #midilist, I transfer every single note to a midilist, chord is a list inside midilist
    global midilist  
    midilist = []
    
    #this is the list of monotonic sequences, we get aList from divider
    global aList  
    aList = []
    
    #rfingers represents the fingering for right hands
    global rfingers  
    rfingers = []
    
    #intervalbook contains all the possible fingers we use for a increasing sequence
    global intervalbook  
    intervalbook = {0: [[1,6],[2,6],[3,6],[4,6],[5,6],[6,6]],
                    1: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[3,5],[4,5],
                       [3,1],[2,1]],
                    2: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[3,5],[4,5],
                       [3,1],[2,1],[4,1]],
                    3: [[1,3],[1,2],[1,4],[2,4],[2,3],[3,4],[3,5],[2,1]],
                    4: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[3,5],[2,1],
                       [3,1]],
                    5: [[1,2],[1,3],[1,4],[2,4],[2,5],[2,3],[3,5]],
                    6: [[1,3],[1,4],[1,2],[2,4],[2,5]],
                    7: [[1,5],[1,4],[1,3],[1,2],[2,5],[2,4]],
                    8: [[1,5],[1,4],[1,3],[2,5]],
                    9: [[1,5],[1,4],[1,3],[3,5]],
                    10:[[1,5],[1,4],[1,3]],
                    11:[[1,5],[1,4]],
                    12:[[1,5],[1,4]]}
    
    #intervalbook2 contains all the possible fingers we use for a decreasing sequence
    global intervalbook2 
    intervalbook2 = {0: [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
                    1: [[2,1],[4,1],[3,2],[3,1],[1,2],[1,3],[1,4],[4,2],[4,3],[5,3],[5,4]],
                    2: [[2,1],[5,4],[3,2],[4,3],[3,1],[4,2],[4,1],[1,2],[1,3],[5,3]],
                    3: [[3,1],[2,1],[4,1],[3,2],[4,2],[4,3],[5,3],[1,2],[1,3]],
                    4: [[3,1],[2,1],[4,1],[3,2],[4,2],[5,3],[4,3],[1,2]],
                    5: [[3,1],[4,1],[2,1],[5,2],[4,2],[5,3],[3,2]],
                    6: [[3,1],[4,1],[4,2],[2,1],[5,2]],
                    7: [[5,1],[4,1],[3,1],[2,1],[4,2]],
                    8: [[5,1],[4,1],[3,1],[5,2]],
                    9: [[5,1],[4,1],[3,1],[5,3]],
                    10: [[4,1],[5,1],[3,1]],
                    11: [[4,1],[5,1]],
                    12: [[4,1],[5,1]]}