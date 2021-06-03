def solution(name):
    answer = 0
    visit = [0 if i!='A' else 1 for i in name]
    cur, dist = 0, 0
    visit[0] = 1
    while any(i==0 for i in visit):
        for idx in range(1, len(name)):
            if visit[cur + idx] == 0:
                visit[cur + idx] = 1
                cur += idx
                dist += idx
                break
            if visit[cur - idx] == 0:
                visit[cur - idx] = 1
                cur -= idx
                dist += idx
                break
    for i in name:
        diff = ord(i)-ord('A')
        if diff <= 13:
            answer += diff
        else:
            answer += 26 - diff
    return answer + dist