from collections import deque

def solution(land):
    W = len(land[0])
    H = len(land)
    pos = [0] * W

    checked = []
    for i in range(H):
        checked.append([False] * W)

    def bfs(i, j):
        q = deque([[i,j]])
        amount = 0
        width = set()
        while q:
            x, y = q.popleft()
            amount += 1
            width.add(y)
            #상하좌우, not checked -> check, 1인 경우 더하기
            if x > 0 and not checked[x-1][y] and land[x-1][y]:
                checked[x-1][y] = True
                q.append([x-1,y])
            if y > 0 and not checked[x][y-1] and land[x][y-1]:
                checked[x][y-1] = True
                q.append([x,y-1])
            if x < H-1 and not checked[x+1][y] and land[x+1][y]:
                checked[x+1][y] = True
                q.append([x+1,y])
            if y < W-1 and not checked[x][y+1] and land[x][y+1]:
                checked[x][y+1] = True
                q.append([x,y+1])

        for w in width:
            pos[w] += amount


    for x in range(H):
        for y in range(W):
            if not checked[x][y] and land[x][y]:
                checked[x][y] = True
                bfs(x, y)

    return max(pos)