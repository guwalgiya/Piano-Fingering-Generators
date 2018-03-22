def main(file_path):
    piece = converter.parse(file_path)
    testing_midi = xml_to_midi_for_testing.main(piece)
    testing_midi_array = np.array(testing_midi)
    testing_interval_array = np.diff(testing_midi_array)

    first_two_fingers = [1, 2, 3]

    a = first_two_fingers[0]
    b = testing_interval_array[0]
    c = first_two_fingers[1]
    d = testing_interval_array[1]
    e = first_two_fingers[2]
    f = testing_interval_array[2]

    first_testing_input = [a,b,c,d,e,f]
    return testing_interval_array, first_testing_input