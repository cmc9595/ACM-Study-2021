def solution(s):
    left, right = 0, 0
    for i in s:
        if i == '(':
            left += 1
        else:
            right += 1
        if right > left:
            return False
    return False if right != left else True