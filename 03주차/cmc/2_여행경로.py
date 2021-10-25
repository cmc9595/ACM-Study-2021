from copy import deepcopy
def dfs(tickets, visit, path, answer):
    if all(i==1 for i in visit):
        answer.append(deepcopy(path))
        return
    temp = []
    for idx, ticket in enumerate(tickets):
        if path[-1]==ticket[0] and visit[idx] == 0:
            temp.append((ticket[1], idx))
    for dest, idx in temp: # for문 돌며 하나씩 탐색
        visit[idx] = 1
        path.append(dest)
        dfs(tickets, visit, path, answer)
        visit[idx] = 0 # 뒤로 돌아가
        path.pop()
def solution(tickets):
    answer, path = [], ["ICN"]
    visit = [0 for _ in range(len(tickets))]
    dfs(tickets, visit, path, answer)
    answer = sorted(answer)
    return answer[0]