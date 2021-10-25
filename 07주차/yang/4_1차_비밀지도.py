import re
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        src = bin(arr1[i]|arr2[i])[2:].zfill(n)
        src = re.sub('0',' ', src)
        src = re.sub('1','#', src)
        answer.append(src)
    return answer
