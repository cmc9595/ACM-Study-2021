def solution(m, n, puddles):
    answer = 0
    a = [[0] * m for _ in range(n)]
    
    for puddle in puddles:
        a[puddle[1]-1][puddle[0]-1] = '*'
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                a[i][j]=1
                continue
            if a[i][j] == '*': continue
            if j > 0:
                if a[i][j-1] != '*': a[i][j] += a[i][j-1]

            if i > 0:
                if a[i-1][j] != '*': a[i][j] += a[i-1][j]            
    
    return a[n-1][m-1] % 1000000007
