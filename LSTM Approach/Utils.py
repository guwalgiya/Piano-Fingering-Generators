def elapsed(sec):
    if sec<60:
        return str(sec) + " sec"
    elif sec<(60*60):
        return str(sec/60) + " min"
    else:
        return str(sec/(60*60)) + " hr"

def generateNewState(old_state, finger_pred, new_interval):
    return old_state[2:]+[finger_pred, new_interval]