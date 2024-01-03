def solution(n):
    a=set(range(3,n+1,2))
    for i in range(3,n+1,2):
        if i in a:
            a-=set(range(i*2,n+1,i))
    return len(a)+1