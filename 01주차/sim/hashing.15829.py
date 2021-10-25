n = int(input())
charL = input()
print(sum([((ord(char)-96) * (31**i)) for i, char in enumerate(charL)])%1234567891)
