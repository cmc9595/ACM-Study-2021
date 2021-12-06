def solution(gems):
    answer = float('inf')
    l = []
    start, end = 0, 0
    for i in range(0, len(gems)+1):
        
        end = i
        cur = gems[start:end]
        
        if len(cur)>=2 and cur[-1]==cur[0]:
            start += 1
            while gems[start]==gems[start+1] and end-start>1:
                start += 1
        print(start, end, gems[start:end])
    return 0

inputs = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    	["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
]

for input in inputs:
    solution(input)
    print()