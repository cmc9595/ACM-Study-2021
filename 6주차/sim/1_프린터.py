def solution(priorities, location):
    answer = []
    loc = []
    loc_re = []
    re = []
    leng = len(priorities)


    for i in range(0,leng):
        loc.append(i)

    pop_idx = 0
    while True:
        if not priorities:
            break
        select = priorities[0];
        sel_idx = loc[0]
        priorities.remove(priorities[0])
        loc.remove(loc[0])
        u_flag = False
        for ie in priorities:
            if ie > select:
                u_flag = True
                break

        if u_flag == True:
            priorities.append(select)
            loc.append(sel_idx)
        else:
            re.append(select)
            loc_re.append(sel_idx)


    for i in range(0,leng):
        if location == loc_re[i]:
            ret = i+1
            break
    return ret
