from itertools import combinations
def solution(relation):
    l = list(zip(*relation))
    arr = [j for i in range(1, len(l)+1) for j in list(combinations(l, i))][::-1]
    answer = []
    while arr:
        i = arr.pop()
        cand = list(zip(*i)) # tuplize
        if len(cand) == len(set(cand)):
            tmp = []
            for j in arr:
                if j!=i and set(j).issuperset(set(i)):
                    tmp.append(j)
            for j in tmp:
                arr.remove(j)
            answer.append(i)
    return len(answer)