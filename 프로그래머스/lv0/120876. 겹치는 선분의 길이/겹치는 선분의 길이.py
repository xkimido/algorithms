def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    # https://velog.io/@damin1025/프로그래머스-겹치는-선분의-길이