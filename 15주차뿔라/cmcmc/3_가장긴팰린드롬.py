def solution(s):
    answer = 0
    for i in range(1, len(s)+1):
        for j in range(len(s)+1-i):
            p = s[j:j+i]
            if p==p[::-1]:
                answer = max(answer, len(p))
    return answer