# 2개 이하로 다른 비트
def solution(numbers):
    answer = []

    for i in numbers:

        if i % 2 == 0:
            answer.append(i + 1)
        else:
            b = bin(i)[2:]
            b = list(b)

            for j in range(len(b)-1, -1, -1):
                if b[j] == '0':
                    b[j] = '1'
                    b[j+1] = '0'
                    b[0] = '0b' + b[0]
                    break

                if j == 0 and b[j] == '1':
                    b[0] = '0b10'
                    break

            answer.append(int(''.join(b), 2))

    return answer
