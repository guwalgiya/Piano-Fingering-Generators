from GetESTFingering import getFormattedTestFilenames, prepareInputList, trainHmm, runHmm, FHMM1, FHMM2
from ConvertToCsv import convertToCsv
# generate train list
prepareInputList()
# train hmm
trainHmm()
# get est results with trained hmm
test_filenames = getFormattedTestFilenames()
runHmm(test_filenames, FHMM2, default=False)
convertToCsv(input_dir='./ESTResults/selfTrained/'+FHMM1+'/', output_dir='./JPESTResults/selfTrained/'+FHMM1+'/')