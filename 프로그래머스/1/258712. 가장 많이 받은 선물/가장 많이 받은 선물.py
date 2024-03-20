def solution(friends, gifts):
    d={}
    for i in friends:
        d[i]=dict(zip(friends,[0]*len(friends))) # -:받기 +:주기
    for j in gifts:
        a,b=j.split()
        d[a][b]+=1
        d[b][a]-=1
    d2=dict(zip(friends,[0]*len(friends)))
    for p in friends:
        for q in friends:
            if p==q:
                continue
            if d[p][q]>0:
                d2[p]+=1
            elif d[p][q]==0:
                if sum(list(d[p].values()))>sum(list(d[q].values())):
                    d2[p]+=1
    return max(list(d2.values()))