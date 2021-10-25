def solution(progresses, speeds):
    answer = []
    check = [0 for _ in range(len(progresses))]
    while any(i < 100 for i in progresses):
        # 하루 경과
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        for i in range(len(progresses)):
            if all(progresses[j] >= 100 for j in range(i + 1)) and check[i] == 0:
                check[i] = 1
                cnt += 1
        if cnt >= 1:
            answer.append(cnt)
    return answer