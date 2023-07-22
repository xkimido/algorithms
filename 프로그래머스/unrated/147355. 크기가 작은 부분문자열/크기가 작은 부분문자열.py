def solution(t, p):
    t_len = len(t)
    p_len = len(p)
    result = 0

    for i in range(t_len - p_len + 1):
        substring = t[i:i + p_len]
        if int(substring) <= int(p):
            result += 1

    return result
