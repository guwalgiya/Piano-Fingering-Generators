function y = rightDownCalculator(seq,starter)
    downTrans = csvread('rightDownState.csv');
    downEmission = csvread('rightDownEmission.csv');
    switch starter
        case 1
            p = [0.5,0.5,0,0,0,0,0,0,0,0,0,0];
        case 2
            p = [0,0,1,0,0,0,0,0,0,0,0,0];
        case 3
            p = [0,0,0,0.5,0.5,0,0,0,0,0,0,0];
        case 4
            p = [0,0,0,0,0,1/3,1/3,1/3,0,0,0,0];
        case 5
            p = [0,0,0,0,0,0,0,0,0.25,0.25,0.25,0.25];
    end
    Transhat = [0 p; zeros(size(downTrans,1),1) downTrans];
    Transhat
    Emishat = [zeros(1,size(downEmission,2));downEmission];    
    y = hmmviterbi(seq,Transhat,Emishat);
    
end
