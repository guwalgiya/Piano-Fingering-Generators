import settings

def chordFingers(chord):
    print(settings.intervalbook[2])
    n = len(chord)
    poss = []
    if n == 2:
        poss = settings.intervalbook[chord[1] - chord[0]][:]
        return poss
    if n in [3,4]:
        for i in range(n - 1):
            n = len(poss)
            if i == 0:  # 现在讨论的是第一个元素
                temp1 = settings.intervalbook[chord[i + 1] - chord[i]][:]  # 查阅音程对应的可用指法， temp包括所有可用指法
            else:  # 不是第一个元素的情况
                temp2 = settings.intervalbook[chord[i + 1] - chord[i]][:]
                for pair1 in temp1:
                    for pair2 in temp2:
                        if pair1[-1] == pair2[0]:
                            poss.append(pair1 + pair2[1:])
                if n < len(poss):
                    poss = poss[n:]
                else:
                    for pairs in poss:
                        pairs.append(1)
                        # print('upcurrent',poss)
    if len(chord) == 5:
        return [1,2,3,4,5]

