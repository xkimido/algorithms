import math
def solution(n):
    x = math.sqrt(n)
    if x != int(x):
        return -1
    return math.pow(x+1, 2)