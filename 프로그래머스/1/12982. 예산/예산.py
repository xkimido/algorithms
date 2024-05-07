def solution(d, budget):
    s = 0
    j = 0
    d.sort()

    for i in range(len(d)):
        s += d[i]
        if s > budget:
            break
        else:
            j += 1

    return j