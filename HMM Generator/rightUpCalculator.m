function y = rightUpCalculator(seq,starter)
    upTrans = csvread('rightUpState.csv');
    upEmission = csvread('rightUpEmission.csv');
    switch starter
        case 1
             p = [0.25,0.25,0.25,0.25,0,0,0,0,0,0,0,0];
        case 2
             p = [0,0,0,0,0.25,0.25,0.25,0.25,0,0,0,0];
        case 3
             p = [0,0,0,0,0,0,0,0,1/3,1/3,1/3,0];
        case 4
             p = [0,0,0,0,0,0,0,0,0,0,0,1];
        case 5
             p = [0,0,0,0,0,0,0,0,0,0,0,0];
    end
    Transhat = [0 p; zeros(size(upTrans,1),1) upTrans];
    Emishat = [zeros(1,size(upEmission,2));upEmission];    
    y = hmmviterbi(seq,Transhat,Emishat);
end