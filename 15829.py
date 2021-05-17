L = int(input())
line = list(input())
s = 0
for idx, c in enumerate(line):
    s += (ord(c)-96)*(31**idx)
    s %= 1234567891
print(s)