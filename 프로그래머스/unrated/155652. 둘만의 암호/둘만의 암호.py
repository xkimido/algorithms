def solution(s, skip, index):
    alphas = [chr(a) for a in range(ord("a"), ord("z")+1) if chr(a) not in skip]
    return "".join([alphas[(alphas.index(a) + index) % len(alphas)] for a in s])