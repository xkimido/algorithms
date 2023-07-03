def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            answer.append(numbers[i] * numbers[j])
    return sorted(answer)[-3]