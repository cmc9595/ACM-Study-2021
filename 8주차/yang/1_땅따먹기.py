def solution(land):

    for row in range(1, len(land)):
        land[row][0] += max(land[row-1][1], land[row-1][2], land[row-1][3])
        land[row][1] += max(land[row-1][0], land[row-1][2], land[row-1][3])
        land[row][2] += max(land[row-1][0], land[row-1][1], land[row-1][3])
        land[row][3] += max(land[row-1][0], land[row-1][1], land[row-1][2])

    answer = max(land[-1])
    
    return answer
