def dfs(start, node, n, v):
    for i in node[start]:
        if v[i] == 0:
            v[i] = 1
            dfs(i, node, n, v)
            # v[i] = 0 # 되돌아나옴

def solution(n, computers):
    node = [[] for _ in range(n)]
    for idx, i in enumerate(computers):
        for jdx, j in enumerate(i):
            if j == 1 and jdx != idx:
                node[idx].append(jdx)

    v = [0 for _ in range(n)]
    cnt = 0
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            dfs(i, node, n, v)
            cnt += 1
    return cnt