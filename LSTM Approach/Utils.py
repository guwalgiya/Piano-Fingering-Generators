def elapsed(sec):
    if sec<60:
        return str(sec) + " sec"
    elif sec<(60*60):
        return str(sec/60) + " min"
    else:
        return str(sec/(60*60)) + " hr"

def generateNewState(old_state, finger_pred, new_interval, normalization=True):
    if normalization:
        return old_state[2:]+[finger_pred/5.0, new_interval]
    else:
        return old_state[2:]+[finger_pred, new_interval]
    
def generateNewStateBi(old_state, finger_pred, new_interval, normalization=True):
    if normalization:
        return old_state[2:-1] + [finger_pred/5.0, old_state[-1], new_interval]
    else:
        return old_state[2:-1] + [finger_pred, old_state[-1], new_interval]

def slide_window(input_list, window_size):
    train_input = []
    train_label = []
    return train_input, train_label