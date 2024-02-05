N, M = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            three =  lst[i] + lst[j] + lst[k]
            if three > M:
                continue
            else:
                nlst.append(three)
print(max(nlst))