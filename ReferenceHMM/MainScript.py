from GetESTFingering import getFormattedTestFilenames, prepareInputList, trainHmm, runHmm, FHMM1, FHMM2, FHMM3
from ConvertToCsv import convertToCsv
# generate train list
# prepareInputList()
# train hmm
# trainHmm()
# # get est results with trained hmm
test_filenames = getFormattedTestFilenames()
print(test_filenames)
runHmm(test_filenames, FHMM1, default=False)
convertToCsv(input_dir='./ESTResults/selfTrained/'+FHMM1+'/', output_dir='./JPESTResults/selfTrained/'+FHMM1+'/')
runHmm(test_filenames, FHMM2, default=False)
convertToCsv(input_dir='./ESTResults/selfTrained/'+FHMM2+'/', output_dir='./JPESTResults/selfTrained/'+FHMM2+'/')
runHmm(test_filenames, FHMM3, default=False)
convertToCsv(input_dir='./ESTResults/selfTrained/'+FHMM3+'/', output_dir='./JPESTResults/selfTrained/'+FHMM3+'/')