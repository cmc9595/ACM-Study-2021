from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    for name, kind in clothes:
        dic[kind].append(name)
    for key, val in dic.items():
        answer *= len(val)+1
    return answer-1