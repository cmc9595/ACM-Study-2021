import datetime
def solution(lines):
    answer, mylist = [], []
    for line in lines:
        date, duration = " ".join(line.split()[:-1]), float(line.split()[-1][:-1])
        end = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        start = end - datetime.timedelta(seconds=duration - 0.001)
        mylist.append([start, end])

    for i in range(len(mylist)):
        start, end = mylist[i][1], mylist[i][1] + datetime.timedelta(seconds=1)
        cnt = 0
        for j in range(len(mylist)):
            if start <= mylist[j][0] < end or start <= mylist[j][1] <= end or (
                    mylist[j][0] <= start and end <= mylist[j][1]):
                cnt += 1
        answer.append(cnt)

    return 1 if not answer else max(answer)