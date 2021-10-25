def solution(s):
    answer = True
    l = []
    for c in s:
        l.append(c)
        if c == ')':
            pair = False
            while len(l) > 0:
                x = l.pop()
                if x == '(':
                    pair = True
                    break
                if len(l) == 0 and pair == False:
                    return False
    if len(l) > 0:
        return False
        

    return True
