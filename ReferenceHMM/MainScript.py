from GetESTFingering import getFormattedTestFilenames, prepareInputList, runHmm, FHMM1, FHMM2
from ConvertToCsv import convertToCsv
# # generate train list
# prepareInputList()
# get est results with trained hmm
test_filenames = getFormattedTestFilenames()
runHmm(test_filenames, FHMM2, default=False)
convertToCsv(input_dir='./ESTResults/selfTrained/'+FHMM2, output_dir='./JPESTResults/selfTrained/'+FHMM2)