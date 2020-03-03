import subprocess
import os
import pickle

INPUT_DIR = './SourceCode/FingeringFiles/'
OUTPUT_DIR = './ESTResults/'

FHMM1 = 'FHMM1'
FHMM2 = 'FHMM2'

def prepareInputList():
    train_filenames = pickle.load(open("./train_filenames.pkl", "rb"))
    train_filenames = [filename.split('_')[0] for filename in train_filenames]
    with open('input_list.txt', 'w') as writer:
        for filename in train_filenames:
            writer.write("%s\n" % filename)

def getFormattedTestFilenames():
    test_filenames = pickle.load(open("./test_filenames.pkl", "rb"))
    test_filenames = [filename.replace('csv', 'txt') for filename in test_filenames]
    return test_filenames

def trainHmm():
    subprocess.call(['./train_hmm.sh'])

def runHmm(filenames, hmm_type, default=False):
    for filename in filenames:
        if default:
            subprocess.call(['./run_'+hmm_type+'.sh', INPUT_DIR+filename, OUTPUT_DIR+'/default/'+hmm_type+'/'+filename])
        else:
            subprocess.call(['./run_trained_'+hmm_type+'.sh', INPUT_DIR+filename, OUTPUT_DIR+'/selfTrained/'+hmm_type+'/'+filename])
