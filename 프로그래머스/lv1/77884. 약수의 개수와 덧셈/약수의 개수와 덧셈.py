def solution(left, right):
    def discr(n):
        li = [i for i in range(1,n+1) if n%i==0]
        return n if len(li)%2==0 else -n

    s=0
    for i in range(left, right+1):
        s += discr(i)

    return s