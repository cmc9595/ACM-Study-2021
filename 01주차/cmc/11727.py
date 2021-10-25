n = int(input())
a = [0 for _ in range(n+2)]
a[0] = 0
a[1] = 1
a[2] = 3
if n>=3:
    for i in range(3, n+2):
        a[i] = a[i-2]*2 + a[i-1]
print(f'{a[n]%10007}')