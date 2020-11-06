def subset(k):
    global cnt
    if k == N:
        res, flag = 0, False
        for i in range(N):
            if visited[i]:
                flag = True
                res += arr[i]
        if res == S and flag:
            cnt += 1
        return
    else:
        visited[k] = 1
        subset(k+1)
        visited[k] = 0
        subset(k + 1)

N, S = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
visited = [0] * N
subset(0)
print(cnt)