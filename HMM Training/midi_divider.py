
#this function divides the midilist into monotonic sequences
def main(midi_list):
    midi_list_monotonic = [] 
    
    while(len(midi_list) > 1):
        
        if len(midi_list) == 1:
            return midi_list_monotonic
        midi_list, midi_list_monotonic = increasing(midi_list, midi_list_monotonic) #找递增序列
        
        if len(midi_list) == 1:
            return midi_list_monotonic
        midi_list, midi_list_monotonic = uniform(midi_list, midi_list_monotonic) #找不变序列
        
        if len(midi_list) == 1:
            return midi_list_monotonic
        midi_list, midi_list_monotonic = decreasing(midi_list, midi_list_monotonic) #找递减序列
    
    return midi_list_monotonic


def increasing(l, l_new): #used in dividing
    i = 0
    j = 1
    while (validTest(i,j,l) == 0): #True:递增，不变； False:递减
        i = i + 1
        j = j + 1
        if j == len(l): #已碰到最后一个音或和弦
            break
    if j == 1:
        return l, l_new
    l_new.append(l[0:j]) #找到一个单调序列
    return l[j-1:], l_new #保留上一个序列的最后一个音，清楚其他上一个序列的音

def uniform(l, l_new):
    i = 0
    j = 1
    while (validTest(i,j,l) == 1):
        i = i + 1
        j = j + 1
        if j == len(l):
            break
    if j == 1:
        return l, l_new
    l_new.append(l[0:j])
    return l[j-1:], l_new

def decreasing(l, l_new): #used in dividing
    i = 0
    j = 1
    while (validTest(i,j,l) == 2): #判定结果 True递减， False递增或不变
        i = i + 1
        j = j + 1
        if j == len(l): #已碰到最后一个音或和弦
            break
    if j == 1:
        return l, l_new
    l_new.append(l[0:j])  #找到一个单调序列
    return l[j-1:], l_new #保留上一个序列的最后一个音，清楚其他上一个序列的音

def validTest(i,j,l): #used in increasing() and decreasing()

    #Comparison between two notes
    if (type(l[i]) is tuple) and (type(l[j]) is tuple):
        if l[i][0] < l[j][0]:
            return 0
        elif l[i][0] == l[j][0]:
            return 1
        else:
            return 2

    #Comparison between a chord and a note
    if (type(l[i]) is list) and (type(l[j]) is tuple):
        if l[i][0][0] < l[j][0]:
            return 0
        elif l[i][0][0] == l[j][0]:
            return 1
        else:
            return 2

    #Comparison between a note and a chord
    if (type(l[i]) is tuple) and (type(l[j]) is list):
        if l[i][0] < l[j][0][0]:
            return 0
        elif l[i][0] == l[j][0][0]:
            return 1
        else:
            return 2

    #Comparison between two chords
    if (type(l[i]) is list) and (type(l[j]) is list):
        if l[i][0][0] < l[j][0][0]:
            return 0
        elif l[i][0][0] == l[j][0][0]:
            return 1
        else:
            return 2
