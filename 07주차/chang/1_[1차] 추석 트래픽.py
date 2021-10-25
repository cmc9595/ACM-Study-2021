import datetime

def solution(lines):

    answer = 0

    time_edge_list = []
    for line in lines:

        t = line.split()[1]
        diff = line.split()[2].replace("s","")

        time_end = datetime.datetime.strptime(t,"%H:%M:%S.%f")
        time_start = time_end - datetime.timedelta(milliseconds=(int(float(diff)*1000-1)))

        temp_list = []
        temp_list.append(time_start)
        temp_list.append(time_end)

        time_edge_list.append(temp_list)

    for i, src in enumerate(time_edge_list):
        answer_temp = 0
        for j, dest in enumerate(time_edge_list):
    
            if time_edge_list[j][0] > time_edge_list[i][0] - datetime.timedelta(seconds=1) and time_edge_list[j][0] <= time_edge_list[i][0]:
                answer_temp += 1
            elif time_edge_list[j][1] > time_edge_list[i][0] - datetime.timedelta(seconds=1) and time_edge_list[j][1] <= time_edge_list[i][0]:
                answer_temp += 1
            elif time_edge_list[j][0] <= time_edge_list[i][0] - datetime.timedelta(seconds=1) and time_edge_list[j][1] >= time_edge_list[i][0]:
                answer_temp += 1

            if answer_temp > answer:
                answer = answer_temp

    return answer
