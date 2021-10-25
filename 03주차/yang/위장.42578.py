from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for c in clothes:
        dic[c[1]]+=1
    for elm in dic:
        answer *= (dic[elm]+1)
        
    return answer - 1
