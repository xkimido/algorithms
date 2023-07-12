def solution(score):
    total = [sum(score[i]) for i in range(len(score))]
    return [sorted(total, reverse=True).index(i) + 1 for i in total]