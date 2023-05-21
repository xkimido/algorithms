def solution(emergency):
    a = emergency
    b = sorted(a, reverse=True)
    result = []
    for i in a:
        result.append(b.index(i) + 1)

    return result


def solution(emergency):
    s_emergency = sorted(emergency, reverse=True)
    return [s_emergency.index(i) + 1 for i in emergency]

def solution(emergency):
    s_emergency = sorted(emergency, reverse=True)
    return list(map(lambda x:s_emergency.index(x)+1, emergency))