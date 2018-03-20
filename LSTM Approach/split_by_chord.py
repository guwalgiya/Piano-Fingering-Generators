def main(midi_list, normalization=True):
    song_interval = []
    song_finger   = []
    start         = 0
    stop          = 0
    while stop < len(midi_list):
        if type(midi_list[stop]) is list:
            seq                      = midi_list[start:stop]
            seq_interval, seq_finger = seq_filter(seq, normalization)
            if seq_interval == []:
                pass
            else:
                song_interval.append(seq_interval)
                song_finger.append(seq_finger)
            
            
            stop  = stop + 1
            start = stop
        else:
            stop = stop + 1
    try:
        seq = midi_list[start:stop]
        seq_interval, seq_finger = seq_filter(seq, normalization)
        if seq_interval == []:
            pass
        else:
            song_interval.append(seq_interval)
            song_finger.append(seq_finger)
        # print('Work')
    except:
        pass
    return song_interval, song_finger

def seq_filter(seq, normalization=True):
    seq_interval = []
    seq_finger = []
    if len(seq) < 3:
        return seq_interval, seq_finger
    else:
        for i in range(len(seq) - 1):
            seq_interval.append(seq[i + 1][0] - seq[i][0])
            seq_finger.append( seq[i][1] )
            
        seq_finger.append(seq[i+1][1])
        if normalization:
            return [x / 12.0 for x in seq_interval], [x / 5.0 for x in seq_finger]
        else:
            return seq_interval, seq_finger
