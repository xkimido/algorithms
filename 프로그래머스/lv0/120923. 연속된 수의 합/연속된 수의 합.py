def solution(num, total):
    start = (total - (num-1) * num // 2) // num
    return [start + i for i in range(num)]
