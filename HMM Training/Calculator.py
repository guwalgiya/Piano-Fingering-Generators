from music21 import *
import settings
import assign

def work():
    f = 0
    for i in range(len(settings.aList)-1):
        if i < len(settings.aList):
            print(settings.aList[i])
            if settings.aList[i][0] is int:
                try:
                    f = settings.rfingers[-1][-1] #f是上一个单调序列的最后一个音的指法
                except:
                    f = 0 #第一个序列
            if settings.aList[i][0] is list:
                try:
                    f = settings.rfingers[-1][-1]
                except:
                    f = [0] * len(settings.rfingers[i][0])
            print(f)
            print('xxxxxxxxxxxxxxxxxxxxxxx')

            if classifier(settings.aList[i][0], settings.aList[i][-1]) in [1,4,7,10]:  #递增
                assign.up(settings.aList[i],settings.aList[i+1],f) #输入f作为本序列的第一个音的指法
            elif classifier(settings.aList[i][0], settings.aList[i][-1]) in [2,5,8,11]:  #不变
                assign.uniform(settings.aList[i],settings.aList[i+1],f) #输入f作为本序列的第一个音的指法
            else: #递减
                assign.down(settings.aList[i],settings.aList[i+1],f) #输入f作为本序列的第一个音的指法

    #以下几行意义一样，只是在处理最后两个数列而已
    f = settings.rfingers[-1][-1]
    if settings.aList[-1][-1] - settings.aList[-1][0] >= 0:
        assign.up(settings.aList[-1], [], f)
    else:
        assign.down(settings.aList[-1], [], f)

def simplelist():
    print(settings.rfingers)
    for i in range(len(settings.rfingers)-1):
        if settings.rfingers[i][-1] == 6:
            settings.rfingers[i][-1] = settings.rfingers[i+1][0]

    #这个方法用来把所有的sublist拆除，只剩下指法数字
    simplelist = [settings.rfingers[0][0]]
    for phrase in settings.rfingers:
        simplelist = simplelist + phrase[1:]

    settings.rfingers = simplelist
    print(settings.rfingers)
    settings.rfingers.reverse()
    for i in range(len(settings.rfingers)-1):
        if settings.rfingers[i + 1] == 6:
            settings.rfingers [i + 1] = settings.rfingers[i]
    settings.rfingers.reverse()

def classifier(a,b):
    if(a is int) and (b is int):
        if a - b < 0:
            return 1
        elif a - b == 0:
            return 2
        elif a - b > 0:
            return 3
    elif(a is int) and (b is list):
        if a - b[0] < 0:
            return 4
        elif a - b[0] == 0:
            return 5
        elif a - b[0] > 0:
            return 6
    elif (a is list) and (b is int):
        if a[0] - b < 0:
            return 7
        elif a[0] - b == 0:
            return 8
        elif a[0] - b > 0:
            return 9
    else:
        if a[0] - b[0] < 0:
            return 10
        elif a[0] - b[0] == 0:
            return 11
        elif a[0] - b[0] > 0:
            return 12