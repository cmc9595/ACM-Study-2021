def solution(n, words):
    answer = []

    answer.append(0)
    answer.append(0)
    
    players = []
    prewords = []
    
    for i in range(n):
        players.append([])
    
    for i,word in enumerate(words):
        
        pnum = i%n
        
        if word in prewords:
            answer[0] = pnum + 1
            answer[1] = len(players[pnum]) + 1
            break
        elif i != 0:
            pword = prewords[-1]
            if pword[-1] != word[0]:
                answer[0] = pnum + 1
                answer[1] = len(players[pnum]) + 1
                break
        
        prewords.append(word)
        pnum = i % n
        players[pnum].append(word)
        
        

    return answer
