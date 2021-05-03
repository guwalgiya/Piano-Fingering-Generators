#! /bin/bash

if [ $# -ne 2 ]; then
echo "Error in usage: ./run_FHMM3.sh in_fin.txt out_fin.txt"
exit 1
fi

Infile=$1
Outfile=$2

./SourceCode/Binary/FingeringHMM3_Run ./Params/hmm3_param.txt ${Infile} ${Outfile} 0.448 0.292 0.194 0.470 0.504 -5

