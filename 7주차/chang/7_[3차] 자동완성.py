def solution(words):
    answer = 0

    words.sort()

    s_index = 0

    for i in range(len(words) - 1):
        j = 0
        for j in range(len(words[i])):
            if words[i][j] != words[i + 1][j]:
                break
        if s_index < j + 1:
            answer += j + 1
        else:
            answer += s_index
        s_index = j + 1
        if words[i][j] == words[i+1][j]:
            s_index += 1

    answer += s_index

    return answer
