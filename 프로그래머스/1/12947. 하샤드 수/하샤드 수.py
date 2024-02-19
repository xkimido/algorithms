def solution(x):
    return not( x % sum([int(n) for n in str(x)]))