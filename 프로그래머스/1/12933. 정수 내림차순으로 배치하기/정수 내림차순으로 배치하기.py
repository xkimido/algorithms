def solution(n):
    result = list(str(n))
    result.sort(reverse = True)
    
    return int("".join(result))