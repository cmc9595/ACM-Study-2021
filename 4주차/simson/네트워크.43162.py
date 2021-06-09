from collections import deque
def bfs(n, computers, i):
    q = deque()
    sub_network = set()
    for j in range(n):
        if computers[i][j] == 1:
            computers[i][j] = 2
            q.append((i, j))
    if not q:
        sub_network.add(i)
        return
    
    while q:
        x = q.popleft()
        sub_network.add(x[0])
        sub_network.add(x[1])
        
        i = x[1]
        for j in range(n):
            if computers[i][j] == 1:
                computers[i][j] = 2
                q.append((i, j))
        
    return sub_network

def solution(n, computers):
    answer = []
    full = set(i for i in range(n))
    for i in range(n):
        sub_network = bfs(n, computers, i)
        if sub_network:
            full -= sub
            answer.append(sub)
    if full:
        answer.append(full)
    
    return len(answer)
