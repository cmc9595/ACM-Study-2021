def solution(genres, plays):
    answer = []

    times = {}
    for i in range(len(genres)):
        if genres[i] not in times:
            times[genres[i]] = plays[i]
        else:
            times[genres[i]] += plays[i]

    stimes = sorted(times.items(), key=lambda x: -x[1])

    for genre, time in stimes:
        tmp = []
        for i in range(len(genres)):
            if genres[i] == genre:
                tmp.append((plays[i], i))
        tmp = sorted(tmp, key=lambda x: (-x[0], i))
        if len(tmp) >= 2:
            answer.append(tmp[0][1])
            answer.append(tmp[1][1])
        elif len(tmp) == 1:
            answer.append(tmp[0][1])
        else:
            pass
    return answer