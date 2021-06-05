import numpy as np

def solution(key, lock):
    M, N = len(key), len(lock)

    # key zero-padding N-1
    key = np.pad(key, ((N-1, N-1), (N-1, N-1)), 'constant', constant_values = 0)
    # lock 0 1 flip
    lock = 1-np.asarray(lock)
    # N*N key kernel
    for i in range(M-1+N):
        for j in range(M-1+N):
            kernel = [row[j:j+N] for row in key[i:i+N]]
            if np.array_equal(kernel, lock):
                return True
            for k in range(3):
                kernel = np.rot90(kernel)
                if np.array_equal(kernel, lock):
                    return True
    return False