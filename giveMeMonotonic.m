function [y,newX] = giveMeMonotonic(x)
    y = x(1);
    for i = 2 : length(x)
        if x(i) - x(i - 1) > 0
            y = [y,x(i)];
        else
            break
        end
    end
    
    for i = 2 : length(x)
        if x(i) - x(i - 1) == 0
            y = [y,x(i)];
        else
            break
        end
    end
    
    for i = 2 : length(x)
        if x(i) - x(i - 1) < 0
            y = [y,x(i)];
        else
            break
        end
    end
    newX = x(length(y):end);        
end