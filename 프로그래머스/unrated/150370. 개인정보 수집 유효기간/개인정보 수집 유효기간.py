def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    today = today[2] + today[1] * 28 + today[0] * 28 * 12

    dic = {}
    for data in terms:
        code, month = data.split(" ")
        dic[code] = int(month) * 28

    for i in range(len(privacies)):
        day, code = privacies[i].split()
        day = list(map(int, day.split('.')))
        day = day[2] + day[1] * 28 + day[0] * 28 * 12
        if day + dic[code] <= today:
            answer.append(i + 1)

    return answer