from collections import deque

def bfs(q, road, K, costs, graph):
    q.append((1, 0))

    while q:
        point = q.popleft()
        curr = point[0]
        cost = point[1]

        for i in range(1, len(graph)):
            if i != curr and graph[curr][i] != -1:
                value = graph[curr][i]
                if costs[i] > cost+value and cost+value <= K:
                    costs[i] = cost+value
                    q.append((i, cost+value))

    print(costs)
    return len([cost for cost in costs if cost != float('inf')])


def solution(N, road, K):
    costs = [float('inf') for _ in range(N+1)]
    q = deque([])
    graph = [[float('inf') for __ in range(N+1)] for _ in range(N+1)]
    for path in road:
        start = path[0]
        end = path[1]
        cost = path[2]
        if graph[start][end] > cost:
            graph[start][end] = cost
        if graph[end][start] > cost:
            graph[end][start] = cost
    costs[1] = 0

    return bfs(q, road, K, costs, graph)