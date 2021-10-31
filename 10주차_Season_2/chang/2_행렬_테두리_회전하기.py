def solution(rows, columns, queries):
    answer = []


    board = [[x+(y*columns) for x in range(1, columns+1)] for y in range(rows)]
    for query in queries:
        mn = 1e9
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        mn = 1e9
        num = board[x1][y1]
        for i in range(y1+1, y2+1):
            board[x1][i], num = num, board[x1][i]
            mn = min(mn, num)
        for i in range(x1+1, x2+1):
            board[i][y2], num = num, board[i][y2]
            mn = min(mn, num)
        for i in range(y2-1, y1-1, -1):
            board[x2][i], num = num, board[x2][i]
            mn = min(mn, num)

        for i in range(x2-1, x1-1, -1):
            board[i][y1], num = num, board[i][y1]
            mn = min(mn, num)

        answer.append(mn)
    return answer
