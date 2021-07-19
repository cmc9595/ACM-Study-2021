def solution(n):
    answer = ''
    digits = '124'
    while n > 0:
        n -= 1
        answer += digits[n % 3]
        n //= 3
    return ''.join(reversed(list(answer)))
