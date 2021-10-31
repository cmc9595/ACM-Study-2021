# 괄호 변환
def solution(p):
    answer = ''
    u, v = split(p)
    while is_right(u):
        u, v = split(v)
    return make_right_strs(u, v)

def make_right_strs(u, v):
    tmp_str = []
    tmp_str.append('(')

    tu, tv = split(v)
    while is_right(tu):
        tu, tv = split(tv)
    tmp_str.append(tv)
    tmp_str.append(')')
    if len(u) >= 2:
        u = list(u)
        u.pop(0)
        u.pop()
    for c in u:
        tmp_u = []
        if c == '(':
            tmp_u.append(')')
        else:
            tmp_u.append('(')
    tmp_str.append(str(tmp_u))
    return str(tmp_str)

def is_right(strs):
    stack = []
    for ch in list(strs):
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False

def split(strs):
    stack = []
    l = 0
    r = 0
    for ch in strs:
        if ch == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return strs[:l+r], strs[l+r:]
