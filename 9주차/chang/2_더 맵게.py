import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
 
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
      
        if s1 >= K:
            break
        else:
            s3 = s1 + s2*2
            heapq.heappush(scoville,s3)
            answer += 1
            
            if len(scoville) == 1:
                if scoville[0] < K:
                    return -1
                else:
                    break
        
    return answer

