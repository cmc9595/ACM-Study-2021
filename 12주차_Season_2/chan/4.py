# 기지국 설치
import math
def solution(n, stations, w):
    answer = 0
    station_ranges = [(0,0)]
    for s in stations:
        left = s - w if s - w >= 0 else 0
        right = s + w if s + w < n else n
        station_ranges.append((left, right))
    station_ranges.append((n+1,n+1))

    for i in range(len(station_ranges)-1):
        answer += math.ceil((station_ranges[i+1][0] - (station_ranges[i][1] + 1)) / (2*w + 1))

    return answer
