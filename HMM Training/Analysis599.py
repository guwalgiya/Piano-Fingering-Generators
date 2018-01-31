import getKnownFingers
import set599
from music21 import *
import dealUpSeq
import dealDownSeq
import prob
import toCSV

set599.initial()
i = 11
while i < 70:
    sheet = 'CXML599_' + str(i) +  '.xml'
    path = 'C:/Users/GuwalgiyaGuan/Documents/2000.Music Technology Master/7100.Piano Fingering/599/' + sheet
    piece = converter.parse(path)
    getKnownFingers.tomidi(piece)
    getKnownFingers.dividing()
    #now we have aList, in aList we have monotonic sequences like this [(72,1),(76,3)]
    for monoSequence in set599.aList:
        try:
            second = monoSequence[1][0]
            helper = int(second)
        except:
            second = monoSequence[1][0][0]

        try:
            first = monoSequence[0][0]
            helper = int(first)
        except:
            first = monoSequence[0][0][0]

        if second - first > 0:
            dealUpSeq.dealUpSeq(monoSequence)
        elif second - first < 0:
            pass
            dealDownSeq.dealDownSeq(monoSequence)
        else:
            pass
    print('Analysis on 599 No.' + str(i) +' is Done!!! ')
    if i == 18:  #file 19 is broken
        i = i + 2
    else:
        i = i + 1

for key in set599.upState:
    set599.upState[key] = prob.StateProbUp(set599.upState[key])
toCSV.su(set599.upState,'RightUpState.csv')
print('========================================')
print(set599.upState)

for key in set599.downState:
    set599.downState[key] = prob.StateProbDown(set599.downState[key])
toCSV.sd(set599.downState,'RightDownState.csv')
print('========================================')
print(set599.downState)

for key in set599.upEmi:
    set599.upEmi[key] = prob.EmiProb(set599.upEmi[key])
toCSV.eu(set599.upEmi,'RightUpEmission.csv')
print('========================================')
print(set599.upEmi)

for key in set599.downEmi:
    set599.downEmi[key] = prob.EmiProb(set599.downEmi[key])
toCSV.ed(set599.downEmi,'RightDownEmission.csv')
print('========================================')
print(set599.downEmi)
