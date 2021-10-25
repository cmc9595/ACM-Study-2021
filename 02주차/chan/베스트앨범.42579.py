from collections import defaultdict
def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    sum_by_genres = defaultdict(int)
    summary = []
    
    for i in range(len(genres)):
        dic[genres[i]].append((i, plays[i]))
        dic[genres[i]].sort(key = lambda x: x[1], reverse=True)
        sum_by_genres[genres[i]] += plays[i]
        if i == len(genres) - 1:
            for g in sum_by_genres:
                summary.append([g, sum_by_genres[g]])
            summary.sort(key = lambda x:x[1], reverse=True)
            break
    
    for elm in summary:
        answer.append(dic[elm[0]][0][0])
        if len(dic[elm[0]]) > 1:
            answer.append(dic[elm[0]][1][0])
    return answer
