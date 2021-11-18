def solution(numbers):
    def f(x):
        if x%4==3:
            return x + 2**(len(bin(x)[2:].split('0')[-1])-1)
        else:
            return x+1
    return list(map(f, numbers))