def solution(t, p):
    return len([t[i: i+len(p)] for i in range(len(t)-len(p)+1) if int(t[i: i+len(p)]) <= int(p)])