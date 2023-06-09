def solution(array, n):
    array.append(n)
    array.sort()
    
    if n == array[-1]:
        return array[array.index(n) - 1]
    elif n == array[0]:
        return array[array.index(n) + 1]
    elif array[array.index(n)] - array[array.index(n) - 1] < array[array.index(n) + 1] - array[array.index(n)]:
        return array[array.index(n) - 1]
    elif array[array.index(n)] - array[array.index(n) - 1] > array[array.index(n) + 1] - array[array.index(n)]:
        return array[array.index(n) + 1]
    elif n == 1:
        return array[array.index(n) - 1]
    else:
        return array[array.index(n) - 1]