block = [
    [[[1, 1, 1], [0, 0, 1]], [[1, 1], [1, 0], [1, 0]], [[1, 0, 0], [1, 1, 1]], [[0, 1], [0, 1], [1, 1]]],
    [[[1, 1, 1], [1, 0, 0]], [[1, 0], [1, 0], [1, 1]], [[0, 0, 1], [1, 1, 1]], [[1, 1], [0, 1], [0, 1]]],
    [[[0, 1, 0], [1, 1, 1]], [[1, 0], [1, 1], [1, 0]], [[1, 1, 1], [0, 1, 0]], [[0, 1], [1, 1], [0, 1]]]
]
unremovable = block[0][0:2] + block[1][::3] + block[2][1:]


def solution(board):
    N = len(board)
    count, flag = 0, 0
    while flag != 2:
        for j in range(N):
            for i in range(N):
                if i == 0 and board[i][j] != 0:
                    break
                if board[i][j] != 0 and i != 0:
                    board[i - 1][j] = -1  # 검은비가내려와~
                    break
                if i == N - 1:
                    board[i][j] = -1
        to_remove = []
        check_square(2, 3, board, to_remove, N)
        check_square(3, 2, board, to_remove, N)
        if not to_remove:  # 비어있으면
            flag += 1
        else:
            count += len(to_remove)
            remove_square(board, to_remove)
            flag = 0
    return count


def remove_square(board, remove_list):
    for block in remove_list:
        y, x = block[0], block[1]
        width, height = len(block[2][0]), len(block[2])
        for j in range(x, x + width):  # 직사각형 지우기
            for i in range(y, y + height):
                board[i][j] = 0
        for j in range(x, x + width):  # 위에 -1지우기
            for i in range(len(board)):
                if board[i][j] == -1:
                    board[i][j] = 0


def check_square(width, height, board, block_list, N):
    for i in range((N - height) + 1):
        for j in range((N - width) + 1):
            dic = {}
            sq = [row[j:j + width] for row in board[i:i + height]]
            for line in sq:
                for color in line:
                    if color in dic:
                        dic[color] += 1
                    else:
                        dic[color] = 1
            tmp = sorted(dic.items(), key=lambda x: -x[1])
            if len(tmp) <= 2 and tmp[0][0] != 0 and tmp[0][1] == 4 and tmp[1][0] == -1 and tmp[1][
                1] == 2:  # 검은블록 2개 포함 없앨수 있는것 찾기
                for c in range(len(sq)):  # 1, 0으로 변환작업
                    for r in range(len(sq[0])):
                        if sq[c][r] == tmp[0][0]:
                            sq[c][r] = 1
                        else:
                            sq[c][r] = 0
                if sq in block[0] + block[1] + block[2] and sq not in unremovable:  # block 모형 중 하나이면
                    block_list.append((i, j, sq))