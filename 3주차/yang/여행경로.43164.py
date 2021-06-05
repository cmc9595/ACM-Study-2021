from collections import defaultdict
from copy import deepcopy
import heapq

answer = []
def dfs(dic, index, path, n):
    global answer
    if answer:
        return
    if index == n:
        answer = deepcopy(path)
        print(path)
        return path

    if index == 0:
        path.append('ICN')
        for next in sorted(dic['ICN']):
            path.append(next[0])
            next[1] = False
            dfs(dic, index+1, path, n)
            next[1] = True
            path.pop()
    elif index > 0:
        if path[-1] in dic:
            for next in sorted(dic[path[-1]]):
                if next[1] == True:
                    path.append(next[0])
                    next[1] = False
                    dfs(dic, index+1, path, n)
                    next[1] = True
                    path.pop()
    return
    
def solution(tickets):
    global answer
    dic = dict()
    n = 0
    for ticket in tickets:
        if ticket[0] not in dic:
            dic[ticket[0]] = []
            heapq.heappush(dic[ticket[0]], [ticket[1], True])
            n+=1
        else:
            heapq.heappush(dic[ticket[0]], [ticket[1], True])
            n+=1
    dfs(dic, 0, [], n)
    
    return answer
