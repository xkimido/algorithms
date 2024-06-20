def solution(n, m):
    answer = []
    arr1 = []
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i ==0:
            arr1.append(i)
    for i in range(max(n, m), (n*m)+1):
        if i%n == 0 and i%m == 0:
            min_num = i
            break
    max_num = max(arr1)
    answer.append(max_num)
    answer.append(min_num)
    return answer