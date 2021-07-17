from collections import deque
dr = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 상하좌우

def bfs(y, x, m): # manhatton dist <= 2 미만 path
    q = deque([[y, x, [[y, x]]]])
    while q:
        curY, curX, path = q.popleft()
        if 2 <= len(path) <= 3 and m[curY][curX]=='P':
            if len(path)==2:
                return False
            if len(path)==3 and m[path[1][0]][path[1][1]] == 'O':
                return False
            continue
        if len(path)==3:
            continue
        for i in range(4):
            nxtY = curY + dr[i][0]
            nxtX = curX + dr[i][1]
            if (0<=nxtX<5 and 0<=nxtY<5) and ([nxtY, nxtX] not in path):
                q.append([nxtY, nxtX, path + [[nxtY, nxtX]]])
    return True

def checkPlace(m):
    for i in range(5):
        for j in range(5):
            if m[i][j]=='P':
                 if not bfs(i, j, m):
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        m = []
        for r in range(len(place)):
            m.append(list(place[r]))
        if not checkPlace(m):
            answer.append(0)
        else:
            answer.append(1)
    return answer