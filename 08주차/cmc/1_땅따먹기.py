def solution(land):
    dp = land[:]
    for row in range(1, len(land)):
        for col in range(4):
            dp[row][col] += max([val for idx, val in enumerate(dp[row - 1]) if idx != col])

    return max(dp[-1])