def solution(people, limit):
    answer = 0
    up = sorted(list(filter(lambda x:x > limit//2, people)), reverse=True)
    down = sorted(list(filter(lambda x:x <= limit//2, people)))
    
    jdx = 0
    if up and down:
        for idx in range(len(up)):
            if up[idx] + down[jdx] <= limit:
                answer += 1
                jdx += 1
                if jdx == len(down):
                    break
    
    return (len(up) - answer) + answer + (len(down) - answer + 1)//2