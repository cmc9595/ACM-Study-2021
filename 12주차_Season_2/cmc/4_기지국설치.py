def solution(n, stations, w):
    cnt = 0
    prev = 1
    leng = 2*w+1
    stations.append(n+1)
    for cur in stations:
        if cur==stations[0]: # 처음
            dist = cur - w - 1
        elif cur==stations[-1]:
            dist = cur - prev - w - 1
        else:
            dist = cur - prev - 2*w - 1
        
        if dist > 0:
            q = dist//leng
            r = dist%leng
            cnt += q if r==0 else q+1
        prev = cur
    return cnt