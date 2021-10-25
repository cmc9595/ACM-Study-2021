from copy import deepcopy
def check(c):
    return True if 'a' <= c <= 'z' else False

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    l1 = [str1[i:i+2] for i in range(len(str1)-1) if check(str1[i]) and check(str1[i+1])]
    l2 = [str2[i:i+2] for i in range(len(str2)-1) if check(str2[i]) and check(str2[i+1])]
    # 중복 교집합
    intersc = []
    tmp = deepcopy(l2)
    for i in l1:
        if i in tmp:
            tmp.remove(i)
            intersc.append(i)
    # 중복 합집합
    union = l1 + l2  # l1, l2바껴도 union안바낌
    for i in intersc:
        union.remove(i)
    if not l1 and not l2:
        return 1*65536
    else:
        return int((len(intersc)/len(union))*65536)