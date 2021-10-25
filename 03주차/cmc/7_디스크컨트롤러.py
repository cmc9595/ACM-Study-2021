import heapq
def solution(jobs):  # 길이 가장 짧은 것 부터
    answer = 0
    job_len = len(jobs)
    done, current, wait = [], [], []
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    time = 0

    while jobs or wait or current:
        while jobs and time == jobs[0][0]:  # 시간 중복 고려
            heapq.heappush(wait, (jobs[0][1], jobs[0][0]))  # (길이, 시간)
            jobs.pop(0)
        if current:
            if time >= current[0][0] + current[0][1][0]:  # finish work
                done.append([time, current.pop()])
        if not current and wait:  # put work
            current.append([time, heapq.heappop(wait)])
        time += 1

    for i in done:
        answer += i[0] - i[1][1][1]
    return answer // job_len