def get_mappoint(point):
    return (point[0]) * 11 + (point[1]+1) - 1

def solution(dirs):
    answer = 0
    map = [[False for _ in range(121)] for _ in range(121)]

    start_point = [5,5]
    dcol = [1,0,-1,0]
    drow = [0,1,0,-1]

    from_point = 0
    to_point = 0 

    for dir in dirs:
        from_point = get_mappoint(start_point)

        if dir == 'R':
            if start_point[1] < 10:
                start_point = [start_point[0]+drow[0],start_point[1]+dcol[0]]
        elif dir == 'D':
            if start_point[0] < 10:
                start_point = [start_point[0]+drow[1],start_point[1]+dcol[1]]
        elif dir == 'L':
            if start_point[1] > 0:
                start_point = [start_point[0]+drow[2],start_point[1]+dcol[2]]
        elif dir == 'U':
            if start_point[0] > 0:
                start_point = [start_point[0]+drow[3],start_point[1]+dcol[3]]

        to_point = get_mappoint(start_point)

        if map[from_point][to_point] == False and from_point!=to_point:
            map[from_point][to_point] = True
            map[to_point][from_point] = True
            answer += 1

    return answer

print(solution("UDU"))