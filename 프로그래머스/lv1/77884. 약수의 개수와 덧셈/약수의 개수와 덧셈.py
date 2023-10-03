def find(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

def solution(left, right):
    li1 = [i if find(i) % 2 == 0 else -i for i in range(left,right+1)]
    return sum(li1)