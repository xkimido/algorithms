import math

def solution(a, b):
    gcd = math.gcd(a, b)  # 최대공약수 계산
    a //= gcd  # 분자를 최대공약수로 나누기
    b //= gcd  # 분모를 최대공약수로 나누기

    # 분모가 2와 5로만 이루어져 있는지 확인
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    if b == 1:  # 분모가 2와 5로만 이루어져 있다면 유한소수
        return 1
    else:  # 분모에 다른 소인수가 있는 경우 무한소수
        return 2
