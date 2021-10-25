from collections import deque

def solution(cacheSize, cities):

    answer = 0
    cache = deque()

    cities_lower = [ city.lower() for city in cities]

    for city in cities_lower:
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                answer += 5
            else:
                cache.popleft()
                cache.append(city)
                answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer

print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))