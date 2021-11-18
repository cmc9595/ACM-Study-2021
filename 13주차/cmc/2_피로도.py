def solution(k, dungeons):
    answer = []
    def dfs(dun, k):
        nonlocal answer
        if not any(i[0]<=k for i in dun):
            answer.append(len(dun))
            return
        
        for i in range(len(dun)):
            if dun[i][0] <= k:
                dfs(dun[:i]+dun[i+1:], k-dun[i][1])
        
    dfs(dungeons,k)
    return len(dungeons) - min(answer)