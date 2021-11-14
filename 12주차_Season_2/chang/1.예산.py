def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget = budget-i
        if budget < 0 :
            break
        answer = answer + 1
    return answer
