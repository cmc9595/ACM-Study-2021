from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(i, idx) for idx, i in enumerate(priorities)])
    while q:
        out = q.popleft()
        if any(elem > out[0] for elem, idx in q):
            q.append(out)
        else:
            answer += 1
            if out[1]==location:
                break
    return answer