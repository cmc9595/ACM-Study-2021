def solution(enroll, referral, seller, amount):
    
    referdict = {}
    sumdict = {}
    
    for i,v in enumerate(enroll):
        referdict[v] = referral[i]
        sumdict[v] = 0

    for i,v in enumerate(seller):
        
        cur = v
        money = amount[i]*100
        while True:
            
            parent = referdict[cur]
            sumdict[cur] += money - money//10
            
            if parent == '-':
                break
            else:
                money = money//10
                cur = parent
        
    answer = []
    for v in enroll:
        answer.append(sumdict[v])
 
    
    return answer
