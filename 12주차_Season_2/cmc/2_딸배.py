import heapq
def dijkstra(start, graph, n):
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, node = heapq.heappop(heap)
        for next_node, next_dist in graph[node]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                heapq.heappush(heap, (distance[next_node], next_node))
                #print(dist, node, next_node, next_dist)
    return distance
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for node1, node2, dist in road:
        graph[node1].append((node2, dist))
        graph[node2].append((node1, dist))
        
    answer = dijkstra(1, graph, N)
    return len(list(filter(lambda x:x<=K, answer)))