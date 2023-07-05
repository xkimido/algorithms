def solution(my_string):
    num = ""
    total_sum = 0

    for char in my_string:
        if char.isdigit():  # char가 숫자인지 확인
            num += char
        elif num != "":
            total_sum += int(num)
            num = ""

    # 마지막 숫자가 있는 경우 합산
    if num != "":
        total_sum += int(num)

    return total_sum
