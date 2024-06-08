def solution(arr, div):
    return sorted([n for n in arr if n%div == 0]) or [-1]