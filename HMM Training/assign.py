import settings
import NNrules
import ChordsOriginal

def up(list1,list2,f):
    a = len(list1)   #list1增序列
    poss = [] #poss = possibilities 可用指法的情况
    for i in range(a - 1):
        n = len(poss)
        if i == 0: #现在讨论的是第一个元素
            temp = settings.intervalbook[list1[i+1] - list1[i]][:]  #查阅音程对应的可用指法， temp包括所有可用指法
            if f != 0 and f != 6:
                for pairs in temp:  #针对temp中每一对儿指法
                    if pairs[0] == f: #把所有一号位是f的指法筛选出来
                        poss.append(pairs)
            else:
                poss = temp[:]   #第一个双元素数列，所有情况都可能

            if len(poss) == 0: #如果没有可以匹配的指法
                poss.append([f,1])  #给他拇指
            #print('upinitial',poss)
        else: #不是第一个元素的情况
            temp1 = []
            temp2 = []
            temp1 = poss[:]
            temp2 = settings.intervalbook[list1[i+1] - list1[i]][:]
            for pair1 in temp1:
                for pair2 in temp2:
                    if pair1[-1] == pair2[0]:
                        poss.append(pair1 + pair2[1:])
            if n < len(poss):
                poss = poss[n:]
            else:
                for pairs in poss:
                    pairs.append(1)
            #print('upcurrent',poss)
    #print('upallpossible',poss)
    #print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    settings.rfingers.append(poss[0])

def uniform(list1,list2,f):
    a = len(list1)   #list1增序列
    poss = [] #poss = possibilities 可用指法的情况
    for i in range(a - 1):
        n = len(poss)
        if i == 0: #现在讨论的是第一个元素
            temp = settings.intervalbook[list1[i+1] - list1[i]][:]  #查阅音程对应的可用指法， temp包括所有可用指法
            if f != 0 and f != 6:
                for pairs in temp:  #针对temp中每一对儿指法
                    if pairs[0] == f: #把所有一号位是f的指法筛选出来
                        poss.append(pairs)
            else:
                poss = temp[:]   #第一个双元素数列，所有情况都可能

            if len(poss) == 0: #如果没有可以匹配的指法
                poss.append([f,1])  #给他拇指
            #print('upinitial',poss)
        else: #不是第一个元素的情况
            temp1 = []
            temp2 = []
            temp1 = poss[:]
            temp2 = settings.intervalbook[list1[i+1] - list1[i]][:]
            for pair1 in temp1:
                for pair2 in temp2:
                    if pair1[-1] == pair2[0]:
                        poss.append(pair1 + pair2[1:])
            if n < len(poss):
                poss = poss[n:]
            else:
                for pairs in poss:
                    pairs.append(1)
            #print('upcurrent',poss)
    #print('upallpossible',poss)
    #print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    settings.rfingers.append(poss[0])

def down(list1,list2,f):
    a = len(list1)
    poss = []
    for i in range(a - 1):
        n = len(poss)
        if i == 0:
            temp = settings.intervalbook2[list1[i] - list1[i + 1]][:]
            if f != 0 and f != 6:
                for pairs in temp:
                    if pairs[0] == f:
                        poss.append(pairs)
            else:
                poss = temp[:]
            if len(poss) == 0:
                poss.append([f,1])

        else:
            temp1 = poss[:]
            temp2 = settings.intervalbook2[list1[i] - list1[i + 1]][:]
            for pair1 in temp1:
                for pair2 in temp2:
                    if pair1[-1] == pair2[0]:
                        poss.append(pair1 + pair2[1:])
            if n < len(poss):
                poss = poss[n:]
            else:
                for pairs in poss:
                    pairs.append(1)
    #print('downdone',poss)


    choice = NNrules.downChoice(poss)
    #print(choice)
    #print('+++++++++++++++++++++++++++++++++++++++++++')
    settings.rfingers.append(choice)