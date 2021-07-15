def solution(n):
    answer = []
    q = 0
    r = 0
    while True:
        q = (n-1) // 3
        r = (n-1) % 3
        
        answer.insert(0,{'0':'1', '1':'2', '2':'4'}[str(r)])
        if q==0:
            break
        else:
            n = q
        
    return ''.join(answer)
