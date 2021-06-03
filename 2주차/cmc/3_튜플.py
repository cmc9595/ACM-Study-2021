def solution(s):
    answer = []
    s = s.split('}')
    s = ' '.join(s).split()  # 공원소 제거

    for i in range(len(s)):
        s[i] = list(map(int, s[i][2:].split(',')))
    s = sorted(s, key=lambda x: len(x))  # 길이별로 정렬 1, 2, 3, ..., n

    answer.append(s[0][0])
    for i in range(len(s) - 1):
        answer.append(list(set(s[i + 1]) - set(s[i]))[0])
    return answer