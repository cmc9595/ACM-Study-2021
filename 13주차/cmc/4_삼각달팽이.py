_dr = [(1, 0), (0, 1), (-1, -1)] # ↓ → ↖
def solution(n):
    l = [[0]*n for _ in range(n)]
    cur = (-1, 0)
    dr = 0
    def nxt(dr):
        return (i+j for i, j in zip(cur, _dr[dr]))
    
    for i in range(0, sum(range(n+1))):
        ny, nx = nxt(dr)
        if not (0<=ny<n and 0<=nx<n and l[ny][nx]==0):
            dr = (dr+1)%3
            ny, nx = nxt(dr)
        
        l[ny][nx] = i+1
        cur = (ny, nx)
    return [j for i in l for j in i if j!=0]