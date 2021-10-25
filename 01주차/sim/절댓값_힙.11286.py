import sys
import queue

N = int(input())
inputs = [int(sys.stdin.readline()) for _ in range(N)]
q = queue.PriorityQueue()
def eliminate():
    if q.empty():
        print(0)
        return
    print(q.get()[1])
    return
        
def add(inp:int):
    q.put((abs(inp), inp))
 
for inp in inputs:
    if inp == 0:
        eliminate()
        continue
    add(inp)
