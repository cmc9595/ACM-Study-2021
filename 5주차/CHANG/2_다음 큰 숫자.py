def solution(n):
    answer = 0

    temp = get_binary_one(n)

    while True:
        n += 1
        temp2 = get_binary_one(n)
        if temp==temp2:
            answer = n
            break

    return answer



def get_binary_one(n):
    count = 0

    while n > 1:
        if n%2 == 1:
            count += 1
        n = n//2

    count += 1
    return count
