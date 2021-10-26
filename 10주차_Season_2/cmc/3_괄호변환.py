def solution(p):
    def isRight(s):
        cur = []
        for i in s:
            if len(cur)>=1 and cur[-1]+i=="()":
                cur.pop()
            else:
                cur.append(i)
        return False if cur else True
    
    def divide(w):
        l, r = 0, 0
        for idx, i in enumerate(w):
            if i=='(':
                l += 1
            else:
                r += 1
            if l==r:
                return w[:idx+1], w[idx+1:]
        
    def convert(w):
        if w=="":
            return ""
        u, v = divide(w)
        if isRight(u):
            return u + convert(v)
        else:
            tmp = '(' + convert(v) + ')'
            for i in u[1:-1]:
                tmp += ')' if i=='(' else '('
            return tmp
    
    return convert(p)