import numpy as np
def solution(m, n, board):
    b = np.array([list(row) for row in board])
    while True:
        same = []
        for i in range(m - 1):
            for j in range(n - 1):
                k = b[i:i + 2, j:j + 2]
                if np.all(k == k[0][0]) and k[0][0] != '0':
                    same.append((i, j))
        if not same:
            break
        for i, j in same:
            b[i:i + 2, j:j + 2] = ' '

        tmp = []
        for j in range(n):
            length = len(np.where((b[:, j] == ' '))[0])
            tmp.append(
                np.pad(np.delete(b[:, j], np.where((b[:, j] == ' '))), (length, 0), 'constant', constant_values=0))
        b = np.transpose(np.array(tmp))

    return len(np.where(b == '0')[0])