def solution(keymap, targets):
    answer = []

    for target in targets:
        c = 0
        for t in target:
            r = min(list(map((lambda x: x.index(t) + 1 if t in x else 102), keymap)))
            if r == 102:
                answer.append(-1)
                break
            else:
                c += r
        if r != 102:
            answer.append(c)          

    return answer