import numpy as np

def solution(food_times, k):
    answer = 0
    
    timesum = 0
    food_len = len(food_times)
    
    for v in food_times:
        timesum += v
    if timesum <= k:
        return -1
    
    while True:
        
        food_time = np.array(food_times)
        food_min = np.min(food_time[np.where(food_time>0)])
        
        if food_min*food_len < k:
            
            k -= food_min*food_len
            for i,v in enumerate(food_times):
                food_times[i] -= food_min
            food_len -= 1
            
        else:
            cur = 0
            
            for i in range(k):
                if food_times[cur] <= 0:
                    cur += 1
                cur = (cur+1)%len(food_times)
                
            answer = cur
            break
    return answer+1

print(solution([3,1,2],5))
