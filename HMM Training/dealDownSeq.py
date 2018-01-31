import set599


def dealDownSeq(seq):
    if len(seq) == 2:
        if (type(seq[0]) is not list) and (type(seq[1]) is not list):
            key = str(seq[0][1]) + str(seq[1][1])
            subKey = seq[0][0] - seq[1][0]
            try:
                set599.downEmi[key][subKey] = set599.downEmi[key][subKey] + 1
            except:
                try:
                    set599.downEmi[key][subKey] = 1
                except:
                    set599.downEmi[key] = {}
                    set599.downEmi[key][subKey] = 1
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
                    set599.downState[key][subKey] = set599.downState[key][subKey] + 1
                except:
                    try:
                        set599.downState[key][subKey] = 1
                    except:
                        set599.downState[key] = {}
                        set599.downState[key][subKey] = 1

                key = str(seq[i][1]) + str(seq[i+1][1])
                subKey = seq[i][0] - seq[i+1][0]
                try:
                    set599.downEmi[key][subKey] = set599.downEmi[key][subKey] + 1

                except:
                    try:
                        set599.downEmi[key][subKey] = 1
                    except:
                        set599.downEmi[key] = {}
                        set599.downEmi[key][subKey] = 1

                if i == (len(seq) - 2):  #handle the last two notes
                    key = str(seq[i+1][1]) + str(seq[i+2][1])
                    subKey = seq[i+1][0] - seq[i+2][0]
                    try:
                        set599.downEmi[key][subKey] = set599.downEmi[key][subKey] + 1
                    except:
                        try:
                            set599.downEmi[key][subKey] = 1
                        except:
                            set599.downEmi[key] = {}
                            set599.downEmi[key][subKey] = 1

                    key = str(seq[i][1]) + str(seq[i + 1][1])
                    subKey = str(seq[i + 1][1]) + str(seq[i + 2][1])
                    try:
                        set599.downState[key][subKey] = set599.downState[key][subKey] + 1
                    except:
                        try:
                            set599.downState[key][subKey] = 1
                        except:
                            set599.downState[key] = {}
                            set599.downState[key][subKey] = 1
