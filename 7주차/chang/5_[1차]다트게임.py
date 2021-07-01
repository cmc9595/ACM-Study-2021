import re

def solution(dartResult):
    answer = 0

    splitResult = []
    temp = []

    for i,v in enumerate(dartResult):
        if v == 'S' or v == 'D' or v=='T':
            temp.append(v)
            if i==len(dartResult)-1 :
                splitResult.append(''.join(temp[:]))
                temp = []
            else:
                if dartResult[i+1]!='*' and dartResult[i+1]!="#":
                    splitResult.append(''.join(temp[:]))
                    temp = []

        elif v == '*' or v =='#':
            temp.append(v)
            splitResult.append(''.join(temp[:]))
            temp = []
        else:
            temp.append(v)

    Result = []

    for i, v in enumerate(splitResult):

        check = ''
        num = int(re.split('[SDT]',v)[0])

        if 'S' in v:
            num = pow(num,1)
        elif 'D' in v:
            num = pow(num,2)
        elif 'T' in v:
            num = pow(num,3)

        if '*' in v:
            num *= 2
            check = '*'

            if i>0:
                Result[i-1][0] *= 2
   
        elif '#' in v:
            num *= -1
            check = '#'

        Result.append([num,check])

    for v in Result:
            answer += v[0]    

    return answer


print(solution("1S*2T*3S"))