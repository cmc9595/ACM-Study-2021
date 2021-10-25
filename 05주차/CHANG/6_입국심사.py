def solution(n, times):
    answer = 1000000000*n

    left = 0
    right = 1000000000*n

    while left <= right:
        mid = (left + right)>>1
        val = 0
        for i in times:
            val += int(mid / i)

        if val >= n:
            if answer > mid:
                answer = mid
            right = mid - 1
        else:
            left = mid + 1


    return answer
