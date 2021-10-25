import datetime
def solution(m, musicinfos):
    candidates, target = [], []
    for i in m:
        if i == '#':
            target[-1] += "#"
        else:
            target.append(i)
    for idx, info in enumerate(musicinfos):
        tmp = []
        s, e, title, chord = info.split(',')
        for i in chord:
            if i == '#':
                tmp[-1] += "#"
            else:
                tmp.append(i)

        minute = (datetime.datetime.strptime(e, "%H:%M") - datetime.datetime.strptime(s, "%H:%M")).seconds // 60
        if minute >= len(tmp):  # 전체 여러번 반복
            quo = minute // len(tmp)
            rmdr = minute % len(tmp)
            tmp = tmp * quo + tmp[:rmdr]
        else:  # 부분만 연주
            tmp = tmp[:minute]
        for i in range(len(tmp) - len(target) + 1):
            if target == tmp[i:i + len(target)]:
                candidates.append([title, minute, idx])
                break
    if not candidates:
        return "(None)"
    else:
        candidates = sorted(candidates, key=lambda x: (-x[1], x[2]))
        return candidates[0][0]