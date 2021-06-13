from collections import deque
def bfs(start, results, v):
    q = deque()
    q.append(start)
    reachable = []
    v[start] = 1
    while q:
        cur = q.popleft()
        for start, end in results:
            if cur==start and v[end]==0:
                v[end] = 1
                q.append(end)
                reachable.append(end)
    return reachable
# 가중치 있을때 dijkstra(heapq), 없을때 bfs
def solution(n, results):
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        v = [1 if i==0 else 0 for i in range(n+1)]
        graph[i] += bfs(i, results, v)
    cnt = 0
    for idx in range(1, n+1):
        if len(graph[idx]) + sum([1 if idx in l else 0 for l in graph]) == n-1:
            cnt += 1
    return cnt