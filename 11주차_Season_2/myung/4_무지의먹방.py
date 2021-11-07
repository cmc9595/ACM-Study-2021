def solution(food_times, k):
    l = []
    for idx, val in enumerate(food_times):
        l.append([val, idx])
    l = sorted(l, key=lambda x:x[0])
    
    hap = 0
    length = len(l)
    idx = 0
    for (val, idx) in l:
        val -= hap
        
        if val*length>k:
            idx = k%length
            break
        else:
            k -= val*length
            hap += val
            length -= 1
            if length==0:
                return -1
            
    return sorted(l[::-1][:length], key=lambda x:x[1])[idx][1]+1