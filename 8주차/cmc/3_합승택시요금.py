import heapq
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for start, end, cost in fares:
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    def dijkstra(s, e):
        nonlocal graph
        q = [(0, s)]
        dist = [0 if i == s else float("inf") for i in range(n + 1)]
        while q:
            cur_d, cur = heapq.heappop(q)
            if dist[cur] < cur_d:
                continue
            for to, cost in graph[cur]:
                if cur_d + cost < dist[to]:
                    dist[to] = cur_d + cost
                    heapq.heappush(q, (dist[to], to))
        return dist[e]

    answer = dijkstra(s, a) + dijkstra(s, b)
    for via in range(1, n + 1):
        if via != s:
            answer = min(answer, dijkstra(s, via) + dijkstra(via, a) + dijkstra(via, b))
    return answer