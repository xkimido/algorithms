def solution(absolutes, signs):
    return sum([2*x*y - x for x, y in zip(absolutes, signs)])