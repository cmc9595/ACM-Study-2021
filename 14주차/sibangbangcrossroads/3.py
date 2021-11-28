## 퍼즐조각 채우기
from collections import deque

def solution(game_board, table):
    def check_table():
        nonlocal table
        _blocks = []
        for y in range(N):
            for x in range(N):
                if table[y][x] == 1:
                    items, table = bfs(x, y, table, 1)
                    _blocks.append(items)
        return _blocks

    def check_game_board():
        nonlocal game_board
        _blocks = []
        for y in range(N):
            for x in range(N):
                if game_board[y][x] == 0:
                    items, game_board = bfs(x, y, game_board, 0)
                    _blocks.append(items)
        return _blocks

    def make_block(blocks, _type):
        _blocks = []
        for block in blocks:
            x_lst = [x for x, y in block]
            y_lst = [y for x, y in block]
            min_x, max_x = min(x_lst), max(x_lst)
            min_y, max_y = min(y_lst), max(y_lst)
            block.sort(key=lambda x: (x[1], x[0]))
            new_block = [[0 if _type == 'block' else 1] * (max_x-min_x+1) for _ in range(max_y-min_y+1)]
            for item in block:
                _x, _y = item[0]-min_x, item[1]-min_y
                new_block[_y][_x] = 1 if _type == 'block' else 0
            _blocks.append(new_block)
        return _blocks

    def rotate_block(block):
        rotate_blocks_lst = [block]
        for _ in range(3):
            block = rotate(block)
            rotate_blocks_lst.append(block)
        return rotate_blocks_lst

    def is_fit(board, block):
        BOARD_X_LEN = len(board[0])
        BOARD_Y_LEN = len(board)
        _block_lst = rotate_block(block)
        for _block in _block_lst:
            block_x_len = len(_block[0])
            block_y_len = len(_block)
            is_fit_flag = True
            if BOARD_X_LEN == block_x_len and BOARD_Y_LEN == block_y_len:
                for y in range(BOARD_Y_LEN):
                    _sum = [board[y][x] + _block[y][x] for x in range(BOARD_X_LEN)]
                    if _sum != [1] * BOARD_X_LEN:
                        is_fit_flag = False
                        break
                if is_fit_flag:
                    return True
        return False

    def rotate(block):
        x_len = len(block[0])
        y_len = len(block)
        new_block = [[0] * y_len for _ in range(x_len)]
        for y in range(y_len):
            for x in range(x_len):
                if block[y][x] == 1:
                    new_block[x][y_len-y-1] = 1
        return new_block

    def is_board(x, y):
        if 0 <= x < N and 0 <= y < N:
            return True
        return False

    def bfs(x, y, board, type):
        q = deque()
        q.append((x, y))
        dx = (1, -1, 0, 0)
        dy = (0, 0, 1, -1)
        items = []

        while q:
            x, y = q.popleft()
            items.append((x, y))
            board[y][x] = -1
            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]
                if is_board(tx, ty) and board[ty][tx] == type:
                    q.append((tx, ty))
        return items, board

    def get_board_score(_board):
        score = 0
        for y in range(len(_board)):
            for x in range(len(_board[0])):
                if board[y][x] == 0:
                    score += 1
        return score
    answer = 0
    N = len(table)
    _table = check_table()
    _game_board = check_game_board()
    block_lst = make_block(_table, 'block')
    board_lst = make_block(_game_board, 'board')
    block_visited = [False] * len(block_lst)
    for board in board_lst:
        for i in range(len(block_lst)):
            if block_visited[i]:
                continue
            block = block_lst[i]
            if is_fit(board, block):
                block_visited[i] = True
                answer += get_board_score(board)
                break
    return answer
