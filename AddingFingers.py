from music21 import *
import settings


def adding():
    RHF = settings.rfingers
    for i in range(len(settings.piece)):
        try:
            Hand(i, settings.piece[i], RHF)
            break
        except:
            pass

    #for i in range(len(piece)):
        #try:
            #Hand(index + i, piece[index + i], LHF)
            #break
        #except:
            #pass


def Hand(i, hand, fingerset):
    for j in range(len(hand)):
        if str(type(hand[j])) == "<class 'music21.stream.Measure'>":
            measure = hand[j]
            numberOfFingers = change(i, measure, j, fingerset)
            fingerset = fingerset[numberOfFingers:]


def change(i, measure, j, fingerset):
    x = 0  # x is counting the number of fingers used in this measure
    for k in range(len(measure)):
        if str(type(measure[k])) == "<class 'music21.note.Note'>":
            finger = fingerset[x]
            settings.piece[i][j][k].articulations = [articulations.Fingering(int(finger))]
            x = x + 1

        elif str(type(measure[k])) == "<class 'music21.chord.Chord'>":
            size = settings.piece[i][j][k].multisetCardinality
            fingersubset = fingerset[x:x + size]
            for finger in fingersubset:
                settings.piece[i][j][k].articulations.append(articulations.Fingering(int(finger)))
            x = x + size
    return x