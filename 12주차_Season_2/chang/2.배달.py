from collections import deque

def solution(n, road, k):
    INF=int(1e9)

    distance=[INF]*(n+1)
    distance[1]=0

    graph=[[INF]*(n+1) for _ in range(n+1)]
    for i in road:
        graph[i[0]][i[1]] = min(graph[i[0]][i[1]], i[2])
        graph[i[1]][i[0]] = min(graph[i[1]][i[0]], i[2])

    q=deque()
    q.append(1)

    while q:
        now=q.popleft()
        for next in range(1,n+1):
            if graph[now][next] != INF and distance[next] > distance[now]+graph[now][next]:
                q.append(next)
                distance[next] = distance[now]+graph[now][next]

    result=0
    for i in range(len(distance)):
        if distance[i] <= k:
            result += 1

    return result
