def solution(n):
    A = [0] * n
    A[0] = 1

    if n > 1:
        A[1] = 2

        for i in range(2,n):
            A[i] = A[i-1] + A[i-2]
        answer = A[n-1]
    else:
        answer = A[0]

    return answer%1234567
