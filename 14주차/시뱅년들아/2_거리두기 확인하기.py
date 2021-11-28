blocks = [[(0, 0), (0, 1), (1, 1)],
         [(0, 0), (0, 1), (-1, 1)],
         [(0, 0), (1, 0), (1, 1)],
         [(0, 0), (1, 0), (1, -1)],
         [(0, 0), (0, -1), (1, -1)],
         [(0, 0), (0, -1), (-1, -1)],
         [(0, 0), (-1, 0), (-1, 1)],
         [(0, 0), (-1, 0), (-1, -1)],
          
         [(0, 0), (0, 1), (0, 2)],
         [(0, 0), (1, 0), (2, 0)],
         [(0, 0), (0, -1), (0, -2)],
         [(0, 0), (-1, 0), (-2, 0)],
          
         [(0, 0), (0, 1)],
         [(0, 0), (0, -1)],
         [(0, 0), (1, 0)],
         [(0, 0), (-1, 0)]]

def check(m):
    def getString(y, x, block):
        return ''.join([m[y+block[i][0]][x+block[i][1]] if 0<=y+block[i][0]<5 and 0<=x+block[i][1]<5 else '-' for i in range(len(block))])
    
    for i in range(5):
        for j in range(5):
            for block in blocks:
                if getString(i, j, block) in ['POP', 'PP']:
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        m = list(map(list, place))
        if not check(m):
            answer.append(0)
        else:
            answer.append(1)
    return answer