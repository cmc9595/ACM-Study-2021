from datetime import datetime
def int_to_time(n):
    return datetime.strptime(str(n // 60) + ":" + str(n % 60), "%H:%M").strftime("%H:%M")

def time_to_int(time):
    h, m = list(map(int, time.split(':')))
    return h * 60 + m

def solution(n, t, m, timetable):
    timetable = sorted(list(map(time_to_int, timetable)))
    tt = timetable[:]
    bus = [540 + i * t for i in range(n)]
    for i in range(len(bus)):
        passenger = list(filter(lambda x: x <= bus[i], tt))[:m]
        bus[i] = (bus[i], passenger)
        for j in passenger:
            tt.remove(j)

    if len(bus[-1][1]) < m:  # 마지막 버스 자리있음
        return int_to_time(bus[-1][0])
    else:  # 마지막 버스 자리없으면 max[마지막 버스 승객] - 1
        return int_to_time(max(bus[-1][1]) - 1)