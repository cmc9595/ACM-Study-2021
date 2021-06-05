from itertools import permutations, combinations
import math

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    L = [n for n in numbers]

    for i in range(1, len(L)+1):
        answer = answer.union(set(int(n) for n in [''.join(elm) for elm in list(permutations(L,i))] if isPrime(int(n))))

    return len(answer)
