dx = [0, 1, 1, 0]
dy = [1, 0, 1, 0]

def solution(m, n, board):
    answer = 0
    board_ = [ list(str_) for str_ in board ]
    board = board_
    while True:
        d_list = delete(m, n, board)
        
        if len(d_list) == 0:
            break
        answer += len(d_list)
        re_arrange(m, n, board, d_list)
    return answer


def re_arrange(m, n, board, d_list):
    for i, j in d_list:
        board[i][j] = 0

    for i in range(m-2,-1,-1):
        for j in range(n):
            if board[i][j] != 0:
                k = i 
                while k+1 < m:
                    if board[k+1][j] == 0:
                        board[k+1][j] = board[k][j]
                        board[k][j] = 0
                    else:
                        break
                    k += 1
    del d_list
    return

def delete(m, n, board):
    d_list = set()
    for i in range(m):
        for j in range(n):
            T = board[i][j]
            if T == 0:
                continue
            match = 0
            for k in range(3):
                if i + dx[k] < m and j + dy[k] < n:
                    if T != board[i + dx[k]][j + dy[k]]:
                        break
                    else:
                        match += 1
                else:
                    break
            if match == 3:
                for k in range(4):
                    d_list.add((i + dx[k], j + dy[k]))
                
    return d_list

