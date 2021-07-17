import numpy
l = [[1, 1, 2], [3, 1, 1], [3, 4, 5]]
print(len(set([j for i in l for j in i])))

for i in l:
    print(i)
print()

for i in l[:2, :2]:
    print(i)