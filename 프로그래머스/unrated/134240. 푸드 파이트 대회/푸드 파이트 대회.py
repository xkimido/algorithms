def solution(food):
    first = ''.join(str(foodNumber) * (quantity // 2) for foodNumber, quantity in enumerate(food))
    second = first[::-1]
    answer = first + '0' + second

    return answer