import sys
input = sys.stdin.readline
T = int(input())
sys.setrecursionlimit(1000000)
def dfs(m, v, x, y, M, N):
    for next_x, next_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if 0 <= next_x < M and 0 <= next_y < N and m[next_y][next_x] == 1 and v[next_y][next_x] == 0:
            v[next_y][next_x] = 1
            dfs(m, v, next_x, next_y, M, N)

for _ in range(T):
    M, N, K = map(int, input().split())
    m = [[0 for _ in range(M)] for _ in range(N)]
    v = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        m[Y][X] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if m[y][x] == 1 and v[y][x] == 0:
                dfs(m, v, x, y, M, N)
                cnt += 1
    print(f'{cnt}')