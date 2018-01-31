import settings
import tomidi
import Divider
import Calculator
import AddingFingers


#Initialization
settings.initial()

#Transfer Music Notes to Midi
Divider.tomidi()
#print(settings.midilist)

#分解成单调数列
Divider.dividing()
#print(settings.aList)

#Calculator.work()
#Calculator.simplelist()
AddingFingers.adding()

settings.piece.show()