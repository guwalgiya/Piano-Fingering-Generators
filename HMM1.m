clc
clear
midi = [84, 83, 81, 79, 77, 76, 74, 72, 79, 77, 76, 74, 72, 71, 69, 71, 72, 76, 72];
superStarter = 2;  %%user decide it
starter = superStarter;
fingers = [superStarter];
while(length(midi) > 1)
    [rawSeq,midi] = giveMeMonotonic(midi);
    [type,seq] = seqType(rawSeq);
    [seqFinger,starter] = hmmState(seq,type,starter);
    starter
    seqFinger
    fingers = [fingers,seqFinger];  
end
forPy = '['
for i = 1 : length(fingers) - 1
    forPy = strcat(forPy,int2str(fingers(i)),',');
end
forPy = strcat(forPy, int2str(fingers(end)),']')

