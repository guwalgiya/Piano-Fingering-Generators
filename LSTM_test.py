from music21 import converter
import numpy as np
import xml_to_midi_for_testing

piece = converter.parse('LSTM_test.xml')
testing_midi = xml_to_midi_for_testing.main(piece)
testing_midi_array = np.array(testing_midi)
testing_interval_array = np.diff(testing_midi_array)


first_two_fingers = [1,2]

#
#a = first_two_fingers[0] + 300
#b = int( str(testing_interval_array[0])  +    str(first_two_fingers[1])   )
#c = testing_interval_array[1] + 200
#first_testing_input = [a,b,c]
  

a = (first_two_fingers[0] - 1) * 25 + (testing_interval_array[0] + 13) 
b = (first_two_fingers[1] - 1) * 25 + (testing_interval_array[1] + 13) 
first_testing_input = [a,b];
