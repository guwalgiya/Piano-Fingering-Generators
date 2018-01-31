function [type,seq] = seqType(x)
        if x(2) - x(1) > 0
            type = 1;
            
            seq = [x(2) - x(1)];
            for i = 3 : length(x)
                seq = [seq;x(i) - x(i-1)];
            end
            
        elseif x(2) - x(1) == 0
            type = 2;
            seq = zeros(1,length(x));
            
        else
            type = 3;
            seq = [x(1) - x(2)];
            for i = 3 : length(x)
                seq = [seq;x(i-1) - x(i)];
            end
        end
              
end