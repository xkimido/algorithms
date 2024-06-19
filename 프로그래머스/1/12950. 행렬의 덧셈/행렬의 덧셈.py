def solution(A, B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]