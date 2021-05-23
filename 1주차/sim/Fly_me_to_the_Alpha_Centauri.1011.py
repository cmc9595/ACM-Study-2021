import sys
T = int(input())
a = [0] * (10**5 + 1)
a[1] = 2
a[2] = 4
for i in range(3,10**5):
    if i%2 == 0:
        a[i] = a[i-1] + (i//2) + 1
    else:
        a[i] = a[i-1] + (i//2) + 2
while T:
    T -= 1
    x, y = map(int, sys.stdin.readline().split())
    #print(x,y)
    if y - x == 1:
        print(1)
        continue
    elif y - x == 2:
        print(2)
        continue
    else:
        dist = (y-1) - (x+1)
        for i in range(10**5-1):
            if a[i] < dist <= a[i+1]:
                print(i+1+2)
                break

