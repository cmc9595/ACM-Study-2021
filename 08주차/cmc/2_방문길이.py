from collections import defaultdict
direction = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
def solution(dirs):
    path = defaultdict(list)
    answer = 0
    cur = (0, 0)
    for d in dirs:
        nxt = tuple([i+j for i,j in zip(cur, direction[d])])
        if not (-5<=nxt[0]<=5 and -5<=nxt[1]<=5):
            continue
        else:
            if direction[d] not in path[cur]:
                path[cur].append(direction[d])
                path[nxt].append(tuple([i*-1 for i in direction[d]]))
                answer+=1
        cur = nxt
    return answer