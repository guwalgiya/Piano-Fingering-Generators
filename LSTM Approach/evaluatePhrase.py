wrong_combo = { "up"     : [(3,2), (4,2), (4,3), (5,1), (5,2), (5,3), (5,4)],        
                "down"   : [(1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)]} 

def main(interval_list, predicted_fingers, Gt_fingers):
    
    num_abs_true                =  0
    num_abs_false               =  0
    
    # predicted_fingers & Gt_fingers have one more element than interval_list does
    for i in range(len(interval_list)-1):
        if  predicted_fingers[i + 1] == Gt_fingers[i + 1]:
            num_abs_true             += 1
        else:
            num_abs_false            += sanityCheck(interval_list[i], (predicted_fingers[i], predicted_fingers[i + 1]))
        
    return num_abs_true, num_abs_false

def sanityCheck(current_interval, current_finger_combo):
    if current_interval > 0:
        return (current_finger_combo in wrong_combo["up"])
    elif current_interval < 0:
        return (current_finger_combo in wrong_combo["down"])
    else:
        return False
