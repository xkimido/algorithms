def solution(food):
    temp = ''
    for i in range(1, len(food)):
        temp += str(i) * (food[i]//2)
    return temp + '0' + temp[::-1]