def solution(land):
    n, m = len(land), len(land[0])
    visited = [[True]*m for _ in range(n)]
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    oil_cnt = [0]*m
    for i in range(n):
        for j in range(m):
            if land[i][j] and visited[i][j]:
                visited[i][j] = False
                s = [(i,j)]
                col = set()
                oil = 0
                while s:
                    x, y = s.pop()
                    col.add(y)
                    oil += 1
                    for dx, dy in delta:
                        X, Y = x+dx, y+dy
                        if 0<=X<n and 0<=Y<m and land[X][Y] and visited[X][Y]:
                            visited[X][Y] = False
                            s.append((X,Y))
                for y in col:
                    oil_cnt[y] += oil
    return max(oil_cnt)