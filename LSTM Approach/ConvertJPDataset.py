# Convert raw dataset to csv which subject to music21 standard
import os

INPUT_DIR = '../Datasets/PianoFingeringDataset/Result_FHMM1/'
OUTPUT_DIR = '../Datasets/JPResDataset/'

for _, _, filenames in os.walk(INPUT_DIR):
    for filename in sorted(filenames):
        with open(INPUT_DIR+filename, 'r') as finger_data_in, open(OUTPUT_DIR+filename.replace('txt', 'csv'), 'w') as finger_data_out:
            print(OUTPUT_DIR+filename)
            finger_data_in.readline()
            for line in finger_data_in:
                line = line.replace('\t', ',')
                line = line.replace(' ', ',')
                line = line.replace('b', '-')
                finger_data_out.writelines(line)
            