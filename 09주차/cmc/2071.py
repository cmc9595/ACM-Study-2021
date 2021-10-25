import numpy as np
from numpy.lib.function_base import _parse_input_dimensions
"""
N = int(input())
row = list(map(int, input().split()))
col = list(map(int, input().split()))
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
"""
N = 5
row = [1, 3, 2, 3, 1]
col = [0, 2, 2, 2, 4]
d1 = [0, 0, 1, 3, 0, 2, 2, 1, 1] # /
d2 = [0, 0, 0, 2, 3, 2, 1, 2, 0] # \
board = [[-1 for _ in range(N)] for _ in range(N)]

def init():
    for i in range(N):
        for j in range(N):
            if row[i]==0:
                board[i][j] = 0
            if col[j]==0:
                board[i][j] = 0
                
            if d1[i+j]==0:
                board[i][j] = 0
            if d2[(N-1)-(i-j)]==0:
                board[i][j] = 0
def checkRow():
    for i in range(N):
        if board[i].count(1)==row[i]:
            board[i] = [1 if x==1 else 0 for x in board[i]]
        if board[i].count(0)==N-row[i]:
            board[i] = [0 if x==0 else 1 for x in board[i]]

def checkCol():
    global board
    cols = list(zip(*board))
    for i in range(N):
        if cols[i].count(1)==col[i]:
            cols[i] = [1 if x==1 else 0 for x in cols[i]]
        if cols[i].count(0)==N-col[i]:
            cols[i] = [0 if x==0 else 1 for x in cols[i]]
    board = list(zip(*cols))

def checkDiag():
    global board
    tmp = [0 for _ in range(2*N-1)]
    
    
        
def checkDiag_np():
    global board
    for i in range(2*N-1):
        if i < N:
            idx = np.diag_indices_from(board[N-1-i:, :i+1]) # [1, 2, 0, 0, 3]
            tmp = board[N-1-i:, :i+1][idx]
        else:
            idx = np.diag_indices_from(board[:2*N-i-1, i-N+1:])
            tmp = board[:2*N-i-1, i-N+1:][idx]
        
        if np.count_nonzero(tmp) == d2[i]:
            tmp[np.where(tmp!=0)] = 1
        if np.count_nonzero(tmp==1) == d2[i]:
            tmp[np.where(tmp!=1)] = 0
            
    for i in range(2*N-1):
        
        board = np.rot90(board, 1)
        if i < N:
            idx = np.diag_indices_from(board[N-1-i:, :i+1]) # [1, 2, 0, 0, 3]
            tmp = board[N-1-i:, :i+1][idx]
            
        else:
            idx = np.diag_indices_from(board[:2*N-i-1, i-N+1:])
            tmp = board[:2*N-i-1, i-N+1:][idx]
            
        if np.count_nonzero(tmp) == d1[i]:
            tmp[np.where(tmp!=0)] = 1
        if np.count_nonzero(tmp==1) == d1[i]:
            tmp[np.where(tmp!=1)] = 0
        board = np.rot90(board, -1)
    
def printt(bb):
    print()
    for row in bb:
        for i in row:
            print("%2d"%i, end=' ')
        print()
    print()

init()
printt(board)
while any(-1 in i for i in board):
    checkRow()
    printt(board)
    checkCol()
    printt(board)
    #checkDiag()
    break

dr = [[0, 1], [1, 0], [-1, 0], [0, -1]]
v = [[0 for _ in range(N)] for _ in range(N)]
cluster = []

def dfs(Y, X):
    global v, stones
    for drY, drX in dr:
        nxtY = Y + drY
        nxtX = X + drX
        if (0 <= nxtX < N and 0 <= nxtY < N) and v[nxtY][nxtX]==0 and board[nxtY][nxtX]==0:
            v[nxtY][nxtX] = 1
            stones.append((nxtX, nxtY))
            dfs(nxtY, nxtX)
    
for i in range(N):
    for j in range(N):
        if board[i][j]==0 and v[i][j]==0:
            v[i][j] = 1
            stones = [(j, i)]
            dfs(i, j)       
            cluster.append(stones)

for stones in cluster:
    if all(x!=0 and y!=0 for x, y in stones):
        print(len(stones))
        break      