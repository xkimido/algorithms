def solution(left, right):
    return sum(n if (n ** 0.5) % 1 else -n for n in range(left, right + 1))