def solution(land):
    answer = 0

    for i, row in enumerate(land):
        if i > 0 :
            for col in range(4):
                previous_max = 0
                for previous_col in range(4):
                    if previous_col != col and land[i-1][previous_col] > previous_max:
                        previous_max = land[i-1][previous_col]

                land[i][col] += previous_max
                
    answer = max(land[len(land)-1])

    return answer

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])