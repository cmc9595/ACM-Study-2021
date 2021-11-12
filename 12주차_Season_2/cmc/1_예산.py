def solution(d, budget):
    d = sorted(d)
    s = 0
    for idx, i in enumerate(d):
        s += i
        if s > budget:
            return idx
    else:
        return len(d)