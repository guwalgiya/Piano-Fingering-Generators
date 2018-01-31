function [y,starter] = hmmState(seq,type,starter)
    switch (type)
        case 1 %going up
            y = rightUpCalculator(seq,starter);
            dic = [0,12,13,14,15,21,23,24,25,31,34,35,45];
            for i = 1:length(y)
                y(i) = mod(dic(y(i)),10);
            end
            starter = y(end);
            
        case 2 %uniform
            y = ones(1,length(seq)-1)* starter;
            
        case 3 %going down        
            y = rightDownCalculator(seq,starter);
            dic = [0,12,13,21,32,31,43,42,41,54,53,52,51];
            for i = 1:length(y)
                y(i) = mod(dic(y(i)),10);
            end
            starter = y(end);
    end
end

