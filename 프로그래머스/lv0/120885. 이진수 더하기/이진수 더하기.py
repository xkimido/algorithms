def solution(bin1, bin2):
    binary_sum = lambda bin1, bin2 : bin(int(bin1, 2) + int(bin2, 2))
    return binary_sum(bin1, bin2)[2:]