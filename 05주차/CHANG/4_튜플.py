def solution(s):
    answer = []
    s = s[2:len(s)-2]
    newS = s.split("},")

    for i in range(len(newS)):
        temp = ''
        for ss in newS[i]:
            if ss == '{':
                continue
            temp = temp + ss
        newS[i] = temp

    sortedNewS = [[] for _ in range(len(newS))]
    for i in range(len(newS)):
        temp = newS[i].split(",")
        mapTemp = map(int, temp)
        newS[i] = list(mapTemp)
        sortedNewS[len(newS[i])-1] = newS[i]

    dic = {}
    for sss in sortedNewS:
        for n in sss:
            if n in dic:
                continue
            dic[n] = 0
            answer.append(n)

    return answer
