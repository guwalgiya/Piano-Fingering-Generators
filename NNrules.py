def upChoice(poss):
    lessCrossing(poss, 1)


def downChoice(poss):
    poss = lessCrossing(poss, 2)
    return poss[0]

#The first rule: less crossing
def lessCrossing(poss, number):
    d = {}
    if number == 2: #means: sequence is going down
       for combo in poss: #combo = every possibility
           counter = 0
           for i in range(len(combo)-1):
               if combo[i+1] - combo[i] > 0: # I find a cross
                  counter = counter + 1
           try:
               d[counter].append(combo)
           except:
               d[counter] = [combo]


    if number == 1: #means: sequence is going up
        for combo in poss: #combo = every possibility
            counter = 0
            for i in range(len(combo)-1):
                if combo[i] - combo[i+1] > 0: # I find a cross
                   counter = counter + 1
                try:
                    d[counter].append(combo)
                except:
                    d[counter] = [combo]

    leastCrossing = list(d.keys())[0]
    # print(d)
    return d[leastCrossing]