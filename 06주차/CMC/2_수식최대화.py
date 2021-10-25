from collections import defaultdict
from itertools import permutations
def calculate(ll, op_list):
    l = ll[:]
    for op in op_list:
        flag = 1
        while flag:
            flag = 0
            for i in range(0, len(l) - 2, 2):
                if l[i + 1] == op:
                    l[i + 2] = str(eval(l[i] + op + l[i + 2]))
                    l.pop(i)
                    l.pop(i)
                    flag = 1
                    break
    return l[0]
def solution(expression):
    answer, l = [], []
    idx = 0
    op = defaultdict(int)
    for i in range(len(expression)):
        if expression[i] in ['-', '+', '*']:
            l.append(expression[idx:i])
            l.append(expression[i])
            idx = i + 1
            op[expression[i]] += 1
    l.append(expression[idx:])
    for i in list(permutations(op.keys())):
        answer.append(calculate(l, i))
    return max(map(lambda x: abs(int(x)), answer))