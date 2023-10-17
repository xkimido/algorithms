def solution(numbers):
    answer = []
    l = len(numbers)
    for i in range(l):
        for j in range(l):
            if i != j:
                answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))