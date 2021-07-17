import math
def fun(N, A, B, cnt):
    h = N//2
    if A <= h and B <= h:
        return fun(h, A, B, cnt+1)
    elif A <= h and h < B:
        return cnt
    elif B <= h and h < A:
        return cnt
    else: # h < A and h < B:
        return fun(h, A-h, B-h, cnt+1)

def solution(n,a,b):
    exp = int(math.log(n, 2))
    return exp - fun(n, a, b, 0)