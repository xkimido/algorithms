def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0