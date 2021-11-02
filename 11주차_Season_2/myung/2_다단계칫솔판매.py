from collections import defaultdict
def solution(enroll, referral, seller, amount):
    up_dic = {}
    money = defaultdict(int)
    for name, refer in zip(enroll, referral):
        if refer=='-':
            up_dic[name] = 'root'
        else:
            up_dic[name] = refer
    
    for name, cnt in zip(seller, amount):
        cur = name
        tmp = cnt*100
        while cur!='root':
            up = int(tmp/10)
            money[cur] += tmp-up
            tmp = up
            cur = up_dic[cur]
            
            if tmp==0:
                break
    
    return [money[i] for i in enroll]