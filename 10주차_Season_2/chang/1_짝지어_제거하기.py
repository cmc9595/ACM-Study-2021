def solution(s):
    answer = -1
    
    temp = ""
    
    for i,v in enumerate(s):
        if len(temp)==0:
            temp += v
        elif temp[-1] == v:
            temp = temp[:-1]
        else:
            temp += v
            
    if len(temp) == 0:
        answer = 1
    else:
        answer = 0
    
    return answer

print(solution("abbabb"))
