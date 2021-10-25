import sys
from collections import deque, defaultdict
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

def bfs():
    global a, N, M
    while q:
        elm = q.popleft()
        x, y = elm[0], elm[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if a[nx][ny] == 0:
                    continue
                if a[nx][ny] == 1:
                    a[nx][ny] = 2
                    q.append((nx, ny))
                    
T = int(input())
while T != 0:
    N, M, K = map(int, sys.stdin.readline().split())
    cab = []
    for _ in range(K):
        cab.append(list(map(int, sys.stdin.readline().split())))
    a = [[0]*N for _ in range(M)]
    for xy in cab:
        a[xy[1]][xy[0]] = 1

    res = 0
    for xy in cab:
        if a[xy[1]][xy[0]] == 1:
            res += 1
            a[xy[1]][xy[0]] = 2
            q.append((xy[1], xy[0]))
            bfs()
    print(res)
    T -= 1

