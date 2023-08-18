from itertools import combinations
def solution(number):
    return sum([1 for c in list(combinations(number,3)) if not sum(c)])