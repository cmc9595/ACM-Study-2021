from math import factorial as f
def solution(n, k):
    l = list(range(1, n+1))
    answer = []
    k -= 1
    for i in range(n-1, 0, -1):
        q = k//f(i)
        r = k%f(i)
        answer.append(l.pop(q))
        k = r
    answer.append(l.pop())
    return answer