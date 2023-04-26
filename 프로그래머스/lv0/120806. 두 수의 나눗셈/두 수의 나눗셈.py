import math

def solution(num1, num2):
    div_mul = (num1 / num2) * 1000
    answer = math.trunc(div_mul)
    return answer