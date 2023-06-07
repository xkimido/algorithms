def solution(s):
    nums = []
    for num in s.split(' '):
        try:
            nums.append(int(num))
        except:
            nums.pop()
    return sum(nums)