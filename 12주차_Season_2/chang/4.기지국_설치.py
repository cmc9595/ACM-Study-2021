import numpy as np
import math

def solution(n, stations, w):
    answer = 0
    
    field = np.array([False for _ in range(n)])
    
    for n in stations:
        field[(n-1)-w:n+w] = True
    
    count = 0
    counts = []
    for x in np.nditer(field):
        if x == True:
            if count!=0:
                counts.append(count)
            count = 0
        else:
            count += 1
    if count!=0:
        counts.append(count)
        
    print(counts)
        
    for c in counts:
        check = 2*w + 1
        
        answer += math.ceil(c/check)
    
    return answer
