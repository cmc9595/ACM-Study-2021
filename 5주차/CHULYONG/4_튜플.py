def solution(s):
    answer = []
    s = [eval('[' + i + ']') for i in s[2:-2].split('},{')]
    s = sorted(s, key=lambda x: len(x))  # 길이순

    answer.append(s[0][0])
    for i in range(len(s) - 1):
        answer.append(list(set(s[i + 1]) - set(s[i]))[0])
    return answer