from music21 import *

#此方法用于初始化
def initial():


    global midilist  #midilist, I transfer every single note to a midilist, chord is a list inside midilist
    midilist = []

    global aList  #this is the list of monotonic sequences, we get aList from divider
    aList = []

    global rfingers  #rfingers represents the fingering for right hands
    rfingers = []

    global upState
    upState = {}

    global upEmi
    upEmi = {}

    global downState
    downState = {}

    global downEmi
    downEmi = {}

    global pComUp   #possible combination for Up
    pComUp = ['12','13','14','15','21','23','24','25','31','34','35','45']

    global pComDown
    pComDown = ['12','13','21','32','31','43','42','41','54','53','52','51']