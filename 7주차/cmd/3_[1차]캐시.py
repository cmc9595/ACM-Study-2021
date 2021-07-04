# CPU가 데이터를 요청하여 캐시 메모리에 접근했을 때 캐시 메모리가 해당 데이터를 가지고 있다면 이를 '캐시 히트' 또는 캐시 적중
# 해당 데이터가 없어서 DRAM에서 가져와야 한다면 '캐시 미스'라 부른다
# LRU = QUEUE로 구현(First in First out)
# deque(maxlen=) : 첫 아이템 자동삭제
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city not in cache: # miss
            cache.append(city)
            answer += 5
        else: # hit
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer