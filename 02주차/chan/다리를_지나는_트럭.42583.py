from collections import deque
from copy import deepcopy

def solution(bridge_length, weight, truck_weights):
    t = 0
    readyq = deque()
    rest_timeq = deque() 
    doneq = deque()

    for truck in truck_weights:
        readyq.append(truck)
    cur_bridge_weight = weight
    
    while True:
        # is enable pop() from ready_queue?
        if cur_bridge_weight > 0 and len(readyq) > 0:
            if cur_bridge_weight - readyq[0] >= 0:
                rest_timeq.append(bridge_length)
                cur_bridge_weight -= readyq[0]
                doneq.append(readyq.popleft())
        
        # exit condition
        if len(readyq) == 0 and len(rest_timeq) == 0:
            break
        
        # time followed
        for i in range(len(rest_timeq)):
            rest_timeq[i] -= 1
            
        tmp = deepcopy(rest_timeq)
        for i in range(len(tmp)):
            if tmp[i] == 0:
                rest_timeq.popleft()
                cur_bridge_weight += doneq.popleft()
       
        t += 1
    return t+1
