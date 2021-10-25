def solution(dirs):
    start = [0, 0]
    map = set()
    for route in dirs:
        if route == 'L':
            s1, e1 = start[0], start[1] 
            if start[0] > -5:
                start[0] -= 1
            else: continue
            s2, e2 = start[0], start[1]
            map.add((s1,e1,s2,e2))
            map.add((s2,e2,s1,e1))
            pass
        elif route == 'R':
            s1, e1 = start[0], start[1] 
            if start[0] < 5:
                start[0] += 1
            else: continue
            s2, e2 = start[0], start[1]
            map.add((s1,e1,s2,e2))
            map.add((s2,e2,s1,e1))
            pass
        elif route == 'U':
            s1, e1 = start[0], start[1] 
            if start[1] < 5:
                start[1] += 1
            else: continue
            s2, e2 = start[0], start[1]
            map.add((s1,e1,s2,e2))
            map.add((s2,e2,s1,e1))
            pass
        elif route == 'D':
            s1, e1 = start[0], start[1] 
            if start[1] > -5:
                start[1] -= 1
            else: continue
            s2, e2 = start[0], start[1]
            map.add((s1,e1,s2,e2))
            map.add((s2,e2,s1,e1))
            pass
    return len(map)/2
