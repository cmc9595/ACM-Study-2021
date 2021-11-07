def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    
    i = 0
    j = len(people)-1
    
    while i<=j :
        
        if i==j:
            answer = answer + 1
            break
        elif people[i] + people[j] <= limit:
            i = i+1
            j = j-1
            answer = answer + 1
        else:
            i = i+1
            answer = answer + 1

    return answer
