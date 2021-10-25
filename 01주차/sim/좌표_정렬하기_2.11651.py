import sys
import heapq

heap = []

N = int(input())
inputs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
for inp in inputs:
    heapq.heappush(heap, (inp[1], inp[0]))
for _ in range(N):
    y, x = heapq.heappop(heap)
    print(x, y)
