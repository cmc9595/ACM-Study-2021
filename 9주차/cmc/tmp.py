"""
N = int(input())
row = list(map(int, input().split()))
col = list(map(int, input().split()))
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
"""

N = 5
row = [1, 3, 2, 3, 1]
col = [0, 2, 2, 2, 4]
d1 = [0, 0, 1, 3, 0, 2, 2, 1, 1]
d2 = [0, 0, 0, 2, 3, 2, 1, 2, 0]

board = [[0 for _ in range(N)] for _ in range(N)]
for i in board:
    print(i)