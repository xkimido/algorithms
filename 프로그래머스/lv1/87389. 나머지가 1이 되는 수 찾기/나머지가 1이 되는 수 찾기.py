def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer