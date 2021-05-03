#!/bin/sh
./SourceCode/Binary/FingeringHMM1_Train input_list.txt ./SourceCode/FingeringFiles hmm1_param
./SourceCode/Binary/FingeringHMM2_Train input_list.txt ./SourceCode/FingeringFiles hmm2_param
./SourceCode/Binary/FingeringHMM3_Train input_list.txt ./SourceCode/FingeringFiles hmm3_param

rm -r ./Params
mkdir -p ./Params
mv hmm1_param.txt ./Params
mv hmm2_param.txt ./Params
mv hmm3_param.txt ./Params