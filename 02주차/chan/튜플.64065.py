def solution(s):
    answer = []
    length = len(s)
    stack = []
    S = set()
    L = []
    SL = []
    
    for i in range(1,len(s)-1):
        if s[i] == '}':
            stack.reverse()
            S = set()
            string_tmp = ""
            while stack: 
                elm = stack.pop()
                string_tmp += elm
            L.append(string_tmp)
        if s[i] == '{' or s[i] == '}': continue
        stack.append(s[i])
    
    for str in L:
        tmpL = str.split(',')
        if tmpL[0] == '':
            del tmpL[0]
        SL.append(set([int(elm) for elm in tmpL]))
    
    SL.sort(key = lambda x: len(x))
    
    
    for s in SL:
        for elm in s:
            if elm not in answer:
                answer.append(elm)        
    return answer
