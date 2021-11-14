# 예산
def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while d:
        d_min = d.pop()
        if d_min > budget:
            break
        elif d_min <= budget:
            budget -= d_min
            answer += 1
    return answer
