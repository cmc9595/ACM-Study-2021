def solution(n, words):
    dic = {}
    for idx, word in enumerate(words):
        if dic.get(word) or (idx>=1 and words[idx-1][-1]!=words[idx][0]):
            return [idx%n + 1, idx//n + 1]
        else:
            dic[word] = 1
    return [0, 0]