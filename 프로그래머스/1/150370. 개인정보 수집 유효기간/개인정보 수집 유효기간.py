def convertToDay(date, term=0):
    date = date.split('.')
    y = int(date[0])
    m = int(date[1])
    d = int(date[2])

    return y * 336 + (m + term) * 28 + d


def solution(today, terms, privacies):
    answer = []
    data = []
    term = {i.split()[0]:int(i.split()[1]) for i in terms}

    cnt = 1

    for i in privacies:
        date, t = i.split()
        if convertToDay(date,term[t]) <= convertToDay(today):
            answer.append(cnt)
        cnt += 1

    return answer