def solution(bridge_length, weight, truck_weights):
    time = 0
    end, mid, start = [], [], truck_weights
    current = 0
    while start or mid:
        # mid 끝난것 end로
        if mid:
            for i in mid:
                i[1] += 1
            if mid[0][1] == bridge_length:
                end.append(mid[0])
                mid.pop(0)

                # start에서 mid로
        if start:
            if mid:
                if sum(i[0] for i in mid) + start[0] <= weight:
                    mid.append([start[0], 0])
                    start.pop(0)
            else:
                mid.append([start[0], 0])
                start.pop(0)
        time += 1
    return time