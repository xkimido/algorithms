def solution(targets):
    answer = 1
    targets.sort()

    s,e = targets[0]
    for target in targets[1:]:
        if target[0] < e:
            if target[1] < e:
                e = target[1]
            continue
        else:
            s, e = target
            answer += 1



    return answer