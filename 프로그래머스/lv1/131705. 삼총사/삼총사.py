from itertools import combinations
def solution(number):
    return len([case for case in combinations(number, 3) if sum(case) == 0])