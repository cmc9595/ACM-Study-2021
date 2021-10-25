def solution(s):
    cur = []
    for i in s:
        if len(cur)>=1 and i==cur[-1]:
            cur.pop()
        else:
            cur.append(i)
    return 0 if cur else 1