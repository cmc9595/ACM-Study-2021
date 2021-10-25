def solution(n, money):
    length = len(money)
    return count_DP(money, length , n)

def count_DP(money, length, n):
    
    table = [[0 for x in range(length)] for x in range(n+1)]
    
    for i in range(length):
        table[0][i] = 1
   
    for i in range(1, n+1):
        for j in range(length):
            x = table[i - money[j]][j] if i-money[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
    return table[n][length-1]