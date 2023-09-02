from collections import defaultdict

def solution(survey, choices):
    indicator = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    answer = ''
    personality = defaultdict(int)
    for s, c in zip(survey, choices):
        if c < 4:
            personality[s[0]] += (4 - c)
        elif c > 4:
            personality[s[1]] += (c - 4)
    for i in indicator:
        if personality[i[0]] >= personality[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer