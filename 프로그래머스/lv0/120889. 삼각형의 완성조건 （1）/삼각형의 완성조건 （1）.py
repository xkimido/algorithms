def solution(sides):
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[2] else 2