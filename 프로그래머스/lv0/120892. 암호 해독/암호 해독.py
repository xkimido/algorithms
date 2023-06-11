def solution(cipher, code):
    return ''.join([cipher[i - 1] for i in range(code, len(cipher) + 1) if i % code == 0])