from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        s = sum(i)
        chk = True
        for j in range(2, int(s ** 0.5) + 1):
            if s % j == 0:
                chk = False
                break
        if chk is True:
            answer += 1
    return answer