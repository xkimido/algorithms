def solution(my_string):
    nums = [i for i in my_string if i.isdigit()]
    return sum(map(int, nums))