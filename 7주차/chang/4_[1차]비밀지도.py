def change_str(n, m):
    s = ""

    while n > 0:
        bit = pow(2, n-1)
        n -= 1
        res = m & bit
        if (res == 0):
            s += " "
        else:
            s += "#"
    return s

def solution(n, arr1, arr2):
    arr = [  (arr1[i] | arr2[i]) for i in range(0, n) ]
    print(arr)
    answer = [ change_str(n, m) for m in arr ]
    return answer