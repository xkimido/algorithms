def solution(price, money, count):
    # answer = -1
    pay = 0
    for i in range(1, count+1):
        pay += (price * i)
    if money < pay:
        return pay - money
    else:
        return 0