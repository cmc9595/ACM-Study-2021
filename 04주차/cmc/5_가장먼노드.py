# heapq dijkstra
import heapq
def dijkstra(e, n):
    start = 1
    distance = [float('inf') if i != 0 else 0 for i in range(n + 1)]
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (distance[start], start))

    while heap:
        dist, node = heapq.heappop(heap)

        for next_node in e[node]:
            if dist + 1 < distance[next_node]:
                distance[next_node] = dist + 1
                heapq.heappush(heap, (dist + 1, next_node))
    return distance

def solution(n, edge):
    e = [[] for _ in range(n + 1)]
    for node1, node2 in edge:
        e[node1].append(node2)
        e[node2].append(node1)

    answer = dijkstra(e, n)
    return len([i for i in answer if i == max(answer)])