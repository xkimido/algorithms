def solution(n):

    if not 3 <= n <= 1000000 :
        return False

    answer = 2
    while True :
        if n % answer == 1 :
            break
        else :
            answer += 1

    return answer