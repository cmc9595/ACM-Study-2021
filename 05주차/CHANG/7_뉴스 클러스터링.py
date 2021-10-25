def solution(str1, str2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = []
    arr2 = []
    for i in range(len(str1) - 1):
        if str1[i] in alphabet and str1[i+1] in alphabet:
            arr1.append(str1[i:i+2])
        else:
            pass

    for i in range(len(str2) - 1):
        if str2[i] in alphabet and str2[i+1] in alphabet:
            arr2.append(str2[i:i+2])
        else:
            pass

    length1 = len(arr1)
    length2 = len(arr2)
    numerator = 0
    for el in arr1:
        if el in arr2:
            arr2.pop(arr2.index(el))
            numerator += 1

    denominator = length1 + length2 - numerator

    if numerator == 0 and denominator == 0:
        return 65536

    answer = (numerator/denominator) * 65536
    return int(answer)