def solution(n):
    answer = 0
    count_one = bin(n).count('1')
    for i in range(n+1,1000001):
        if bin(i).count('1') == count_one: return i
    return answer
