from collections import defaultdict
direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
def solution(arrows):
    g = defaultdict(list)
    cur = (0, 0)
    answer = 0
    for i in arrows:
        nxt = tuple([a+b for a,b in zip(cur, direction[i])])
        # 한번 지났던 path면 건너뛴다..
        if i in g[cur]:
            cur = nxt
            continue
        else:
            g[cur].append(i)
            if (i+4)%8 in g[nxt]:
                cur = nxt
                continue
        x, y = cur
        # 가로세로위아래
        if i in [0, 2, 4, 6]:
            if len(g[nxt])>0:
                answer += 1
        # 대각
        elif i == 1:
            if len(g[nxt])>0 and 5 not in g[nxt]:
                answer += 1
            if 3 in g[(x, y+1)] or 7 in g[(x+1, y)]:
                answer += 1
        elif i == 3:
            if len(g[nxt])>0 and 7 not in g[nxt]:
                answer += 1
            if 1 in g[(x, y-1)] or 5 in g[(x+1, y)]:
                answer += 1
        elif i == 5:
            if len(g[nxt])>0 and 1 not in g[nxt]:
                answer += 1
            if 7 in g[(x, y-1)] or 3 in g[(x-1, y)]:
                answer += 1
        elif i == 7:
            if len(g[nxt])>0 and 3 not in g[nxt]:
                answer += 1
            if 5 in g[(x, y+1)] or 1 in g[(x-1, y)]:
                answer += 1
        cur = nxt
    return answer
