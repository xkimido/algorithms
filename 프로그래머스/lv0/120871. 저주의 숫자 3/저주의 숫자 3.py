def solution(n):
    count10 = 0
    count3 = 0
    while count10 < n:
        count10 += 1
        count3 += 1
        while count3 % 3 == 0 or '3' in str(count3):
            count3 += 1
    return count3