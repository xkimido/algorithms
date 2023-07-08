from itertools import permutations

def solution(spell, dic):
    combinations = list(permutations(spell))
    
    for combination in combinations:
        word = ''.join(combination)
        if word in dic:
            return 1
    
    return 2