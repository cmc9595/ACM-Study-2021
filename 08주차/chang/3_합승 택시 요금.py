import heapq

n=200
def init(n, fares):
    graph = {}
    for i in range(1, n+1):
        graph[i] = {}
    for i in fares:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]
    return graph


def dijkstra(graph, start):
    distances = {v: [start, float('inf')] for v in graph}
    visited = [0]*(n+1)
    distances[start] = [start, 0]

    queue = []
    heapq.heappush(queue, [start, distances[start][1]])
    while queue:
        current_vertex, current_distance = heapq.heappop(queue)

        if distances[current_vertex][1] < current_distance:
            continue

        for adjacent_node, weight in graph[current_vertex].items():
            distance = current_distance+weight
            if distance < distances[adjacent_node][1]:
                distances[adjacent_node] = [current_vertex, distance]
                heapq.heappush(queue, [adjacent_node, distance])

    return distances


def solution(n, s, a, b, fares):
    graph = init(n, fares)
    distances = dijkstra(graph, s)
    min_distance = distances[a][1]+distances[b][1]
    for i in range(1, n+1):
        if i == a or i == b or i == s:
            pass
        distance = dijkstra(graph, i)
        if min_distance > distance[a][1]+distance[b][1]+distances[i][1]:
            min_distance = distance[a][1]+distance[b][1]+distances[i][1]

    return min_distance