import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    dist = y - x
    leap = 1
    total = 0
    cnt = 0
    """
    while 1:
        if dist - total*2 + 1 < leap:
            total -= leap
            leap -= 1
            break
        leap += 1
        total += leap
        cnt += 1

    print(leap, dist - total*2)
    """

    while total < dist:
        cnt += 1
        total += leap
        if cnt%2 == 0:
            leap += 1
    print(cnt)