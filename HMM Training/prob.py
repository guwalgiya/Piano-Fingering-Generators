import set599

def StateProbUp(d):
    newd = {}
    keyList = list(d.keys())
    for key in keyList:
        if key in set599.pComUp:
            pass
        else:
            d.pop(key)

    for key in d:
        newd[key] = d[key] / sum(d.values())
    return newd

def StateProbDown(d):
    newd = {}
    keyList = list(d.keys())
    for key in keyList:
        if key in set599.pComDown:
            pass
        else:
            d.pop(key)

    for key in d:
        newd[key] = d[key] / sum(d.values())

    return newd

def EmiProb(d):
    newd = {}
    keyList = list(d.keys())
    for key in keyList:
        if key > 12:
            d.pop(key)
        else:
            pass
    for key in d:
        newd[key] = d[key] / sum(d.values())

    return newd