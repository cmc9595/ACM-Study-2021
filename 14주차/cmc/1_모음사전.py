dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
val = [625+125+25+5+1,
      125+25+5+1,
      25+5+1,
      5+1,
      1]
def solution(word):
    answer = 1
    for idx, w in enumerate(word):
        print(idx, w)
        answer+=val[idx]*dic[w]
        
    answer += len(word)-1
    return answer