N = int(input())
l = []
for _ in range(N):
    x, y = map(int, input().split())
    l.append((x, y))
l = sorted(l, key = lambda x: (x[1], x[0]))
for x, y in l:
    print(f'{x} {y}')