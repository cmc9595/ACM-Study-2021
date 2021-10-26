import numpy as np
def solution(rows, columns, queries):
    answer = []
    arr = np.array([[i+j*columns+1 for i in range(columns)] for j in range(rows)])
        
    for y1, x1, y2, x2 in queries:
        l1 = arr[y1-1, x1-1:x2-1]
        l2 = arr[y1-1:y2-1, x2-1]
        l3 = arr[y2-1, x2-1:x1-1:-1]
        l4 = arr[y2-1:y1-1:-1, x1-1]
        
        l = list(l1) + list(l2) + list(l3) + list(l4)
        answer.append(min(map(int, l)))
        l.insert(0, l.pop())
        w = x2-x1
        h = y2-y1
        
        arr[y1-1, x1-1:x2-1] = l[:w]
        arr[y1-1:y2-1, x2-1] = l[w:w+h]
        arr[y2-1, x2-1:x1-1:-1] = l[w+h:w+h+w]
        arr[y2-1:y1-1:-1, x1-1] = l[w+h+w:]
    return answer