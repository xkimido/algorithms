def solution(friends, gifts):
    g_record = {}
    for f1 in friends:
        g_record[f1] = [0,{}]
        for f2 in friends:
            if f1 != f2:
                g_record[f1][1][f2] = 0

    for gift in gifts:
        a,b = gift.split()
        g_record[a][0] += 1
        g_record[a][1][b] += 1
        g_record[b][0] -= 1
        g_record[b][1][a] -= 1
    answer = [0] * len(friends)

    for a, values in g_record.items():
        idx1 = friends.index(a)
        exponent_a = values[0]
        for b, cnt in values[1].items():
            if cnt > 0:
                answer[idx1] += 1
            elif cnt == 0:
                if exponent_a > g_record[b][0]:
                    answer[idx1] += 1

    return max(answer)