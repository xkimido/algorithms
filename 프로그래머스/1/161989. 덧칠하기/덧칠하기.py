def solution(n, m, section):
    answer = 1
    prev = section[0]
    
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1
            
    return answer