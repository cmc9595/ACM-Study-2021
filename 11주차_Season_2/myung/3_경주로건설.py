from collections import deque
def solution(board):
    N = len(board)
    info = [[[float('inf') for _ in range(4)]for _ in range(N)]for _ in range(N)]
    _dr = {0:(0, 1), 1:(-1, 0), 2:(0, -1), 3:(1, 0)} # →↓←↑
    q = deque([(0,0,-1)])
    info[0][0] = [0 for _ in range(4)]
    while q:
        cury, curx, dr = q.popleft()
        for i in range(4):
            nxty = cury + _dr[i][0]
            nxtx = curx + _dr[i][1]
            if 0<=nxty<N and 0<=nxtx<N and board[nxty][nxtx]==0:
                tmp = min(info[cury][curx][i]+100, info[cury][curx][(i+1)%4]+600, info[cury][curx][(i+3)%4]+600)
                if tmp < info[nxty][nxtx][i]:
                    info[nxty][nxtx][i] = tmp
                    q.append((nxty, nxtx, i))
                    
    return min(info[N-1][N-1])