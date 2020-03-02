import os
def convertToCsv(input_dir, output_dir):
    for _, _, filenames in os.walk(input_dir):
        for filename in filenames:
            filename_ = filename.split('.')[0]
            with open(input_dir+filename, 'r') as finger_data_in, open(output_dir+filename_+'.csv', 'w') as finger_data_out:
                finger_data_in.readline()
                for line in finger_data_in:
                    line = line.replace('\t', ',')
                    line = line.replace(' ', ',')
                    line = line.replace('b', '-')
                    finger_data_out.writelines(line)
