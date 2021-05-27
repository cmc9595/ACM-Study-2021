from itertools import combinations

def solution(orders, course):
    answer = []
    dict = {}
    for line in orders:
        for i in range(2, min(len(line)+1, 11)):
            for j in list(combinations(line, i)):
                j = tuple(sorted(j))
                if j in dict:
                    dict[j] += 1
                else:
                    dict[j] = 1
    for num in course:
        tmp = []
        for key, val in dict.items():
            if len(key)==num:
                tmp.append((key, val))
        tmp = sorted(tmp, key=lambda x:x[1], reverse=True)
        if tmp:
            for i in tmp:
                if i[1] == tmp[0][1] and tmp[0][1] >= 2:
                    answer.append("".join(i[0]))
            answer = sorted(answer)
    return answer