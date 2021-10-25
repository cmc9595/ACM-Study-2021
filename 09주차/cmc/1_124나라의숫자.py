dic = {"0": "1", "1": "2", "2": "4"}
def dec_to_ternary(n):
    s = ""
    while True:
        s += str(n % 3)
        if n // 3 == 0:
            break
        n //= 3
    return s[::-1]

def solution(n):
    a, i = 1, 1
    while not a > n:
        a += 3 ** i
        i += 1

    return "".join(list(map(lambda x: dic[x], dec_to_ternary(n - (a - 3 ** (i - 1))).zfill(i - 1))))