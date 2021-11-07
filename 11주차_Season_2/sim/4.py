# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    answer = -1
    queue = []
    x, y = 0, 0

    for i in food_times:
        heapq.heappush(queue, i)

    while queue:
        x = heapq.heappop(queue)

        if k >= (x - y) * (len(queue) + 1):
            k = k - ((x - y) * (len(queue) + 1))
            y = x
        else:
            break

    r = k % (len(queue) + 1)

    for i in range(len(food_times)):
        if food_times[i] > y:
            r = r - 1
            if r < 0:
                answer = i + 1
                break

    return answer

print(solution([3, 1, 2], 5)) # 1
