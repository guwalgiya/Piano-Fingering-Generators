import set599
import csv

def su(d,line):
    file = open(line,'w',newline = '')
    csv_file = csv.writer(file)
    for inSt in set599.pComUp:
        a = []
        for outSt in set599.pComUp:
            try:
                a.append(d[inSt][outSt])
            except:
                a.append(0.001)
        csv_file.writerow(a)

def sd(d,line):
    file = open(line,'w',newline = '')
    csv_file = csv.writer(file)
    for inSt in set599.pComDown:
        a = []
        for outSt in set599.pComDown:
            try:
                a.append(d[inSt][outSt])
            except:
                a.append(0.00001)
        csv_file.writerow(a)

def eu(d,line):
    file = open(line,'w',newline = '')
    csv_file = csv.writer(file)
    for inSt in set599.pComUp:
        a = []
        i = 1
        while(i <= 12):  #i is interval
            try:
                a.append(d[inSt][i])
            except:
                a.append(0)
            i = i + 1
        csv_file.writerow(a)


def ed(d,line):
    file = open(line,'w',newline = '')
    csv_file = csv.writer(file)
    for inSt in set599.pComDown:
        a = []
        i = 1
        while(i <= 12):  #i is interval
            try:
                a.append(d[inSt][i])
            except:
                a.append(0)
            i = i + 1
        csv_file.writerow(a)