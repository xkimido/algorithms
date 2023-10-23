def solution(p,n):
    b=[];a=0
    for m in n:
        d=0;m-=1
        for i in range(0,len(p)):
            if(0!=p[i][m]):d=p[i][m];p[i][m]=0;break
        if(0==d):pass
        elif(0==len(b)):b.append(d)
        elif(d==b[-1]):b.pop();a+=2
        else:b.append(d)
    return a