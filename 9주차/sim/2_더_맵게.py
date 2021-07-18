import heapq
def solution(scoville, K):
    answer = 0
    hq = [] 
    for i in scoville:
        heapq.heappush(hq,i)
    
    while True:
        answer += 1
        if len(hq) >= 2:
            heapq.heappush(hq,heapq.heappop(hq)+(heapq.heappop(hq)*2))
        else:
            return -1
        if hq[0] >= K:
            break
            
    return answer
