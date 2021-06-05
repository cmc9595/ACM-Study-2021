def solution(citations):
    answer = 0
    l = sorted(citations)
    for h in range(len(l)+1):
        bigger = list(filter(lambda x:x>=h, l))
        if len(bigger) >= h:
            answer = h
    return answer