from music21 import *
import settings

#tomidi is the function that transfers the piece into a list of midi numbers
def tomidi():
    for i in range(len(settings.piece)):
        if str(type(settings.piece[i])) == "<class 'music21.stream.Part'>":   #to test if this is music, not title or author or something else
            measurefinder(settings.piece[i]) #piece[i] = rightHand
            break
    return settings.midilist

def measurefinder(righthand): #used in tomidi(), righthand = everything for the right hand
    for i in range(len(righthand)):
        if str(type(righthand[i])) == "<class 'music21.stream.Measure'>": #to test if this is a measure
            insidemeasure(righthand[i]) #righthand[j] = measure

def insidemeasure(measure): #used in measurefinder, measure = the measure we are working on now.
    for i in range(len(measure)): #count the elements in a measure, could be a note or a chord.
        if str(type(measure[i])) == "<class 'music21.note.Note'>": #if this element is a note
            settings.midilist.append(measure[i].midi)
        elif str(type(measure[i])) == "<class 'music21.chord.Chord'>": #if this element is a chord
            chordlist = []
            for p in measure[i]:    #p = part
                chordlist.append(p.midi)     #chordlist is the sub-list reprents a chord
            settings.midilist.append(chordlist) #put the sublist into the midilist

#this function divides the midilist into monotonic sequences
def dividing():
    l = settings.midilist  #l is the local name for settings.midilist
    while(len(l) > 1):
        if len(l) == 1:
            return
        l = increasing(l) #找递增序列
        if len(l) == 1:
            return
        l = uniform(l) #找不变序列
        if len(l) == 1:
            return
        l = decreasing(l) #找递减序列
    return

def increasing(l): #used in dividing
    i = 0
    j = 1
    while (validTest(i,j,l) == 0): #True:递增，不变； False:递减
        i = i + 1
        j = j + 1
        if j == len(l): #已碰到最后一个音或和弦
            break
    if j == 1:
        return l
    settings.aList.append(l[0:j]) #找到一个单调序列
    return l[j-1:] #保留上一个序列的最后一个音，清楚其他上一个序列的音

def uniform(l):
    i = 0
    j = 1
    while (validTest(i,j,l) == 1):
        i = i + 1
        j = j + 1
        if j == len(l):
            break
    if j == 1:
        return l
    settings.aList.append(l[0:j])
    return l[j-1:]

def decreasing(l): #used in dividing
    i = 0
    j = 1
    while (validTest(i,j,l) == 2): #判定结果 True递减， False递增或不变
        i = i + 1
        j = j + 1
        if j == len(l): #已碰到最后一个音或和弦
            break
    if j == 1:
        return l
    settings.aList.append(l[0:j])  #找到一个单调序列
    return l[j-1:] #保留上一个序列的最后一个音，清楚其他上一个序列的音

def validTest(i,j,l): #used in increasing() and decreasing()
    #规则：音高不变算作递增序列

    #Comparison between two notes
    if (type(l[i]) is int) and (type(l[j]) is int):
        if l[i] < l[j]:
            return 0
        elif l[i] == l[j]:
            return 1
        else:
            return 2

    #Comparison between a chord and a note
    if (type(l[i]) is list) and (type(l[j]) is int):
        if l[i][0] < l[j]:
            return 0
        elif l[i][0] == l[j]:
            return 1
        else:
            return 2

    #Comparison between a note and a chord
    if (type(l[i]) is int) and (type(l[j]) is list):
        if l[i] < l[j][0]:
            return 0
        elif l[i] == l[j][0]:
            return 1
        else:
            return 2

    #Comparison between two chords
    if (type(l[i]) is list) and (type(l[j]) is list):
        if l[i][0] < l[j][0]:
            return 0
        elif l[i][0] == l[j][0]:
            return 1
        else:
            return 2


