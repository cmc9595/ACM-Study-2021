# 구명보트
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        max_weight = people.pop()
        if people and max_weight + people[0]<=limit:
            people.popleft()
        answer +=1
    return answer
