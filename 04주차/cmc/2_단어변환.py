def compare(s1, s2):  # 다른 개수 리턴
    return [1 if i != j else 0 for i, j in zip(s1, s2)].count(1)

def bfs(begin, target, words, v):
    q = []
    q.append((begin, 0))

    while q:
        cur, dist = q.pop(0)
        if cur == target:
            return dist
        for idx, word in enumerate(words):
            if v[idx] == 0 and compare(cur, word) == 1:  # can go
                v[idx] = 1
                q.append((word, dist + 1))
    return 0

def solution(begin, target, words):
    v = [0 for _ in range(len(words))]
    return bfs(begin, target, words, v)