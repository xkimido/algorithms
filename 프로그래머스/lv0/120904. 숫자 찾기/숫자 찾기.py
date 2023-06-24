def solution(num, k):
    answer = 0
    l = [i for i in str(num)]
    for i in l:
        if i == str(k):
            answer = l.index(i) + 1
            break
        else:
            answer = -1
    return answer