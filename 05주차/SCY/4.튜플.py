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
            # print(stack)
            while stack: 
                elm = stack.pop()
                string_tmp += elm
            # string_tmp.
            L.append(string_tmp)
        if s[i] == '{' or s[i] == '}': continue
        stack.append(s[i])
    
    
    # print(L)
    for str in L:
        tmpL = str.split(',')
        # print(tmpL)
        if tmpL[0] == '':
            del tmpL[0]
        # print(tmpL)
        SL.append(set([int(elm) for elm in tmpL]))
    
    SL.sort(key = lambda x: len(x))
    # print(SL)
    
    for s in SL:
        for elm in s:
            if elm not in answer:
                answer.append(elm)        
    return answer
