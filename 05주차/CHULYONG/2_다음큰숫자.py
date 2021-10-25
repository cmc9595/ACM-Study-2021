def solution(n):
    num = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == num:
            return n