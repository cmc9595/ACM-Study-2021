def check(mid, times, n):  # 현재 mid에서 인원 원래n보다 크거나 같으면 +1, 작으면 -1 return
    cnt = 0
    for time in times:
        cnt += mid//time
    if cnt >= n:
        return 1
    else:
        return -1
def solution(n, times):
    start = times[0]
    end = times[0]*n
    mid = (start+end)//2
    while end >= start:
        if check(mid, times, n) == 1 and check(mid-1, times, n) == -1:  # 최솟값 찾기위해
            break
        elif check(mid, times, n) == 1:
            end = mid + 1
        else:
            start = mid - 1
        mid = (start + end) // 2
    return mid