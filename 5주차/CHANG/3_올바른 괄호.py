def solution(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return not len(stack)