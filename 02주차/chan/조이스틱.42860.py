def solution(name):
    answer = 0
    # N이 13번으로 기준
    length = len(name)
    making = ["A" for _ in range(length)]
    
    # 처음은 그냥 계산
    answer += 13 - abs(ord(name[0]) - ord('N'))
    making[0] = name[0]
    # print("처음 자리", 13 - abs(ord(name[0]) - ord('N')))
    cursor = 0
    
    
    for i in range(length):
        pos, dist = find_next_pos(cursor, name, making, length)
        if pos:
            cursor = pos
            answer += dist
            # print("자리 차이", dist)
            answer += 13 - abs(ord(name[pos]) - ord('N'))
            # print("캐릭터 차이", 13 - abs(ord(name[pos]) - ord('N')))
            making[pos] = name[pos]
    return answer

def find_next_pos(cursor, name, making, length):

    for width in range(1, length):
        # forward
        if cursor + width < length:
            if name[cursor + width] != making[cursor + width]:
                return cursor + width, width
        elif cursor + width >= length:
            if name[cursor + width - length] != making[cursor + width - length]:
                return cursor + width - length, width
        # backward
        if cursor - width < length and cursor - width >= 0:
            if name[cursor - width] != making[cursor - width]:
                return cursor - width, width
        elif cursor - width < 0:
            if name[length - abs(cursor - width)] != making[length - abs(cursor - width)]:
                return length - abs(cursor - width), width
    return None, None
