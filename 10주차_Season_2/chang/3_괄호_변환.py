def check(s):
    st = 0
    for c in s:
        if(c == '('):
            st = st + 1
        else:
            if(st == 0):
                return 0
            else:
                st = st - 1

    if(st):
        return 0
    return 1

def solution(s):
    ret = ''
    c0 = 0
    c1 = 0
    st = 0
    for i in range(len(s)):
        if(s[i] == '('): c0 = c0 + 1
        else : c1 = c1 + 1

        if(c0 == c1):
            if(check(s[st:i+1]) == 1):
                ret = ret + s[st:i+1]
                st = i + 1
            else:
                tmp = '(' + solution(s[i+1:]) + ')'                
                ret = ret + tmp + s[st+1:i].replace('(','!').replace(')','(').replace('!',')')
                return ret

    return ret
