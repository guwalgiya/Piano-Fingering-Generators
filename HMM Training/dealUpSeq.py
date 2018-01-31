import set599


def dealUpSeq(seq):
    if len(seq) == 2:
        if (type(seq[0]) is not list) and (type(seq[1]) is not list):
            key = str(seq[0][1]) + str(seq[1][1])
            subKey = seq[1][0] - seq[0][0]
            try:
                set599.upEmi[key][subKey] = set599.upEmi[key][subKey] + 1
            except:
                try:
                    set599.upEmi[key][subKey] = 1
                except:
                    set599.upEmi[key] = {}
                    set599.upEmi[key][subKey] = 1
        else:
            pass

    else:
        for i in range(len(seq) - 2):
            if (type(seq[i]) is list) or (type(seq[i + 1]) is list) or (type(seq[i + 2]) is list):
                pass
            else:
                key = str(seq[i][1]) + str(seq[i+1][1])
                subKey = str(seq[i+1][1]) + str(seq[i+2][1])
                try:
                    set599.upState[key][subKey] = set599.upState[key][subKey] + 1
                except:
                    try:
                        set599.upState[key][subKey] = 1
                    except:
                        set599.upState[key] = {}
                        set599.upState[key][subKey] = 1

                key = str(seq[i][1]) + str(seq[i+1][1])
                subKey = seq[i+1][0] - seq[i][0]
                try:
                    set599.upEmi[key][subKey] = set599.upEmi[key][subKey] + 1

                except:
                    try:
                        set599.upEmi[key][subKey] = 1
                    except:
                        set599.upEmi[key] = {}
                        set599.upEmi[key][subKey] = 1

                if i == (len(seq) - 2):  #handle the last two notes
                    key = str(seq[i+1][1]) + str(seq[i+2][1])
                    subKey = seq[i+2][0] - seq[i+1][0]
                    try:
                        set599.upEmi[key][subKey] = set599.upEmi[key][subKey] + 1
                    except:
                        try:
                            set599.upEmi[key][subKey] = 1
                        except:
                            set599.upEmi[key] = {}
                            set599.upEmi[key][subKey] = 1

                    key = str(seq[i][1]) + str(seq[i + 1][1])
                    subKey = str(seq[i + 1][1]) + str(seq[i + 2][1])
                    try:
                        set599.upState[key][subKey] = set599.upState[key][subKey] + 1
                    except:
                        try:
                            set599.upState[key][subKey] = 1
                        except:
                            set599.upState[key] = {}
                            set599.upState[key][subKey] = 1