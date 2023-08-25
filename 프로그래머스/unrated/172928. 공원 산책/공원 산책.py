def solution(park, routes):
    W = len(park[0])
    park = [['X']*(W+2)] + [[*'X'+i+'X'] for i in park] + [['X']*(W+2)]

    x,y = 1,0
    while park[x][y]!='S':
        y += 1
        if y>W:
            x,y = x+1,0

    delta = {k:v for k,v in zip('NEWS',[(-1,0),(0,1),(0,-1),(1,0)])}
    for i in routes:
        v,d = i.split()
        for k in range(1,int(d)+1):
            X,Y = x+k*delta[v][0], y+k*delta[v][1]
            if park[X][Y]=='X':
                break
        else:
            x,y = X,Y
    return [x-1,y-1]