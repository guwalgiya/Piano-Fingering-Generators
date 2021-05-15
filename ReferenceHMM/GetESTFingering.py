import subprocess
import os
import pickle

INPUT_DIR = './SourceCode/FingeringFiles/'
OUTPUT_DIR = './ESTResults/'

INPUT_LIST = 'input_list.txt'

FHMM1 = 'FHMM1'
FHMM2 = 'FHMM2'
FHMM3 = 'FHMM3'

def prepareInputList(train_filenames):
    train_filenames = [filename.split('_')[0] for filename in train_filenames]
    with open(INPUT_LIST, 'w') as writer:
        for filename in sorted(train_filenames):
            writer.write("%s\n" % filename)

def getFormattedTestFilenames(test_filenames):
    test_filenames = [filename.replace('csv', 'txt') for filename in test_filenames]
    return test_filenames

def trainHmm():
    subprocess.call(['./train_hmm.sh'])

def runHmm(filenames, hmm_type, default=False):

    for filename in filenames:
        if default:
            subprocess.call(['./run_'+hmm_type+'.sh', INPUT_DIR+filename, OUTPUT_DIR+'default/'+hmm_type+'/'+filename])
        else:
            subprocess.call(
                [
                    './run_trained_{}.sh'.format(hmm_type), 
                    os.path.join(INPUT_DIR, filename), 
                    os.path.join(
                        OUTPUT_DIR,
                        'selfTrained',
                        hmm_type,
                        filename
                    )
                ]
            )
def convertToCsv(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for _, _, filenames in os.walk(input_dir):
        for filename in filenames:
            filename_ = filename.split('.')[0]
            with open(input_dir+'/' + filename, 'r') as finger_data_in, open(output_dir + '/' + filename_ + '.csv', 'w') as finger_data_out:
                finger_data_in.readline()
                for line in finger_data_in:
                    line = line.replace('\t', ',')
                    line = line.replace(' ', ',')
                    line = line.replace('b', '-')
                    finger_data_out.writelines(line)