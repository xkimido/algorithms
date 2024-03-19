def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    p = [0] * l
    answer = [0] * l
    gr = [[0] * l for i in range(l)]
    for i in gifts:
        a, b = i.split()
        gr[f[a]][f[b]] += 1
    for i in range(l):
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])

    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    return max(answer)