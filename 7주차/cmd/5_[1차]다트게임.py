bonus={'S':1, 'D':2, 'T':3}
def solution(dartResult):
    answer = []
    n = len(dartResult)
    cursor = 0
    for idx, ch in enumerate(dartResult):
        if ch in bonus.keys():
            if idx+1<n and dartResult[idx+1] in ['*','#']:
                line = dartResult[cursor:idx+2]
                option = line[-1]
                total = int(line[:-2])**bonus[line[-2]]
                if option=="*":
                    if answer:
                        answer[-1]*=2
                    total*=2
                else:
                    total*=-1
                answer.append(total)
                cursor = idx+2
            else:
                line = dartResult[cursor:idx+1]
                answer.append(int(line[:-1])**bonus[line[-1]])
                cursor = idx+1
    return sum(answer)