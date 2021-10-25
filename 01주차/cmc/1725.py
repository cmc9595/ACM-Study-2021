import sys
myinput = sys.stdin.readline
N = int(myinput())
l = []
stack = []
mx = 0
for _ in range(N):
    l.append(int(myinput()))
l.append(0)

for idx, i in enumerate(l):
    if idx == 0:  # 첫 기둥
        stack.append((i, idx))  # 높이, idx, 넓이
        mx = i
        continue

    if stack[-1][0] > i:
        while stack and stack[-1][0] > i:
            height, x = stack.pop()
            mx = max(mx, height*(idx-x))
        stack.append((i, x))

    else:  # 크거나 같으면 mx++
        stack.append((i, idx))

print(f'{mx}')