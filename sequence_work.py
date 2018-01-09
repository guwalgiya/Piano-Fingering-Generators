def chord_filter(sequence):
    new_seq = []
    for i in range(len(sequence)):
        if type(sequence[i]) is tuple:
            new_seq.append(sequence[i])
        else:
            new_seq.append((sequence[i][0][0],6))            
    return new_seq

def analysis(sequence):
    if sequence[0][0] < sequence[-1][0]:
        seq_interval_up, seq_finger_up = up_analysis(sequence)
        return seq_interval_up,seq_finger_up, [], []
    elif sequence[0][0] > sequence[-1][0]:
        seq_interval_down, seq_finger_down = down_analysis(sequence)
        return [], [], seq_interval_down, seq_finger_down
    else:
        return [], [], [], []

def up_analysis(sequence):
    seq_interval_up = []
    seq_finger_up = []
    sub_seq_finger_up = []
    sub_seq_interval_up = []
    
    i = 0
    j = 1
    while(i <  len(sequence) - 1):
        if sequence[i][1] == 6 and sequence[i + 1][1] == 6:
            i = i + 1
            if len(sub_seq_finger_up) > 1:
                seq_finger_up.append(sub_seq_finger_up)
                seq_interval_up.append(sub_seq_interval_up)
            j = 1
        elif sequence[i][1] != 6 and sequence[i+1][1] == 6:
            i = i + 1
            if len(sub_seq_finger_up) > 1:
                seq_finger_up.append(sub_seq_finger_up)
                seq_interval_up.append(sub_seq_interval_up)
            j = 1
        elif sequence[i][1] == 6 and sequence[i+1][1] != 6:
            i = i + 1
            if len(sub_seq_finger_up) > 1:
                seq_finger_up.append(sub_seq_finger_up)
                seq_interval_up.append(sub_seq_interval_up)
            j = 1
        else:
            if j == 1:
                sub_seq_finger_up = []
                sub_seq_interval_up = []
                sub_seq_finger_up.append([sequence[i][1],sequence[i+1][1]])
                sub_seq_interval_up.append(sequence[i+1][0] - sequence[i][0])
                i = i + 1
                j = 0
            else:
                sub_seq_finger_up.append([sequence[i][1],sequence[i+1][1]])
                sub_seq_interval_up.append(sequence[i+1][0] - sequence[i][0])
                i = i + 1
                if i ==  (len(sequence) - 1):
                    seq_finger_up.append(sub_seq_finger_up)
                    seq_interval_up.append(sub_seq_interval_up)
           
    
    return seq_interval_up, seq_finger_up



def down_analysis(sequence):
    seq_interval_down = []
    seq_finger_down = []
    sub_seq_finger_down = []
    sub_seq_interval_down = []
    
    i = 0
    j = 1
    while(i <  len(sequence) - 1):
        if sequence[i][1] == 6 and sequence[i + 1][1] == 6:
            i = i + 1
            if len(sub_seq_finger_down) > 1:
                seq_finger_down.append(sub_seq_finger_down)
                seq_interval_down.append(sub_seq_interval_down)
            j = 1
        elif sequence[i][1] != 6 and sequence[i+1][1] == 6:
            i = i + 1
            if len(sub_seq_finger_down) > 1:
                seq_finger_down.append(sub_seq_finger_down)
                seq_interval_down.append(sub_seq_interval_down)
            j = 1
        elif sequence[i][1] == 6 and sequence[i+1][1] != 6:
            i = i + 1
            if len(sub_seq_finger_down) > 1:
                seq_finger_down.append(sub_seq_finger_down)
                seq_interval_down.append(sub_seq_interval_down)
            j = 1
        else:
            if j == 1:
                sub_seq_finger_down = []
                sub_seq_interval_down = []
                sub_seq_finger_down.append([sequence[i][1],sequence[i+1][1]])
                sub_seq_interval_down.append(sequence[i][0] - sequence[i+1][0])
                i = i + 1
                j = 0
            else:
                sub_seq_finger_down.append([sequence[i][1],sequence[i+1][1]])
                sub_seq_interval_down.append(sequence[i][0] - sequence[i+1][0])
                i = i + 1
                if i ==  (len(sequence) - 1):
                    seq_finger_down.append(sub_seq_finger_down)
                    seq_interval_down.append(sub_seq_interval_down)
            
    
    return seq_interval_down, seq_finger_down