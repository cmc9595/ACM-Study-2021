from itertools import permutations
from collections import defaultdict

def is_prime(n):
    if n <= 1:
        return False
    if any(n%i==0 for i in range(2, int(n**0.5)+1)):
        return False
    return True

def solution(numbers):
    dic = defaultdict(int)
    answer = 0
    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers, i)):
            dic[int(''.join(j))] += 1
    for key, val in dic.items():
        if is_prime(key):
            answer += 1
    return answer