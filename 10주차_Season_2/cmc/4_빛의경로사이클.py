def solution(grid):
    dr = {0:(-1, 0), 1:(0, -1), 2:(1, 0), 3:(0, 1)} # up, left, down, right
    answer = []
    row, col = len(grid), len(grid[0])
    visited = [[[0, 0, 0, 0] for j in range(col)] for i in range(row)]
        
    def getNxtPos(curPos, curDir):
        ny, nx = [i+j for i, j in zip(curPos, dr[curDir])]
        if not 0<=nx<=col-1:
            nx %= col
        if not 0<=ny<=row-1:
            ny %= row
        return [ny, nx]
    
    def getNxtDir(curDir, nxtPos):
        nxtNode = grid[nxtPos[0]][nxtPos[1]]
        if nxtNode=='S':
            return curDir
        elif nxtNode=='L':
            return (curDir+1)%4
        elif nxtNode=='R':
            return (curDir-1)%4
        
    def getCycle(startPos, startDir):
        cnt = 1
        curPos, curDir = startPos, startDir
        while True:
            nxtPos = getNxtPos(curPos, curDir)
            nxtDir = getNxtDir(curDir, nxtPos)
            visited[nxtPos[0]][nxtPos[1]][nxtDir] = 1
            if nxtPos==startPos and nxtDir==startDir:
                break
            curPos = nxtPos
            curDir = nxtDir
            cnt += 1
        return cnt
    
    for i in range(row):
        for j in range(col):
            for k in range(4):
                if not visited[i][j][k]:
                    answer.append(getCycle([i, j], k))

    return sorted(answer)