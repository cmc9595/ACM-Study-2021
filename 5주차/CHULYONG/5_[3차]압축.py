from collections import defaultdict
def solution(msg):
    answer = []
    dic = defaultdict(int)
    idx = 1
    for c in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
        dic[c] = idx
        idx += 1

    while msg:
        for i in range(len(msg), 0, -1):
            if dic[msg[:i]]:
                answer.append(dic[msg[:i]])
                tmp = msg[:i]
                msg = msg[i:]

                if msg:
                    dic[tmp + msg[0]] = idx
                    idx += 1
                break
    return answer