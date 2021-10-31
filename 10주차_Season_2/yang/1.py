# 짝지어 제거하기
from collections import deque
def solution(s):
    answer = -1
    stack = deque()

    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
            continue
        if len(stack) > 0 and stack[-1] != ch:
            stack.append(ch)
            continue
        if len(stack) > 0 and stack[-1] == ch:
            stack.pop()
            continue
    if len(stack) == 0:
        return 1
    else:
        return 0
    return answer
