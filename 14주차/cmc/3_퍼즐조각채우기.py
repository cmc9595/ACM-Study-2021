_dy = (0, -1, 0, 1)
_dx = (1, 0, -1, 0)
def solution(game_board, table):
    N = len(table)
    v1 = [[0]*N for _ in range(N)]
    v2 = [[0]*N for _ in range(N)]
    puzzle, slot = [], []
    
    def DFS(i, j, b, v, flag):
        stack = [(i, j)]
        ret = set()
        while stack:
            y, x = stack.pop()
            ret.add((y, x))
            v[y][x] = 1
            for dy, dx in zip(_dy, _dx):
                ny = y + dy
                nx = x + dx
                if 0<=ny<N and 0<=nx<N and b[ny][nx]==flag and v[ny][nx]==0:
                    stack.append((ny, nx))
        return ret
    def makeFit(block): # zero-aim (0,0)
        y, x = zip(*block)
        w, h = min(x), min(y)
        return set([(i-h, j-w) for i, j in block])
    
    def rotate(block): # (0, 0) centered clockwise
        block = set([(-j-1, i) for i, j in block])
        return makeFit(block)
    
    def isMatching(a, b):
        for i in range(4):
            if (a:=rotate(a)) == b:
                return len(a)
        return 0
    # find from table
    for i in range(N):
        for j in range(N):
            if table[i][j]==1 and v1[i][j]==0:
                puzzle.append(makeFit(DFS(i, j, table, v1, 1)))
            if game_board[i][j]==0 and v2[i][j]==0:
                slot.append(makeFit(DFS(i, j, game_board, v2, 0)))
    cnt = 0
    vslot = [0]*len(slot)
    for i in range(len(puzzle)):
        for j in range(len(slot)):
            if (r:=isMatching(puzzle[i], slot[j])) and vslot[j]==0:
                cnt += r
                vslot[j] = 1
                break
    return cnt