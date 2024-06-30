def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    temp = 0
    for i in targets:
        if i[0]<temp:
            continue
        else:
            answer+=1
            temp = i[1]

    return answer