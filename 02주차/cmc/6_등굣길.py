def solution(m, n, puddles):
    arr = [[0 for _ in range(m)]for _ in range(n)]
    arr[0][0] = 1
    for x, y in puddles:
        arr[y-1][x-1] = -1
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            elif arr[i][j] == -1:
                continue
            elif i==0: # 첫행
                arr[i][j] = arr[i][j-1] if arr[i][j-1] != -1 else 0
            elif j==0: # 첫열
                arr[i][j] = arr[i-1][j] if arr[i-1][j] != -1 else 0
            else:
                if arr[i][j-1] == -1 and arr[i-1][j] == -1:
                    arr[i][j] = 0
                elif arr[i][j-1] == -1 and arr[i-1][j] != -1:
                    arr[i][j] = arr[i-1][j]
                elif arr[i][j-1] != -1 and arr[i-1][j] == -1:
                    arr[i][j] = arr[i][j-1]
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[n-1][m-1] % 1000000007