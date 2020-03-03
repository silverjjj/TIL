def dfs(x, s):
    global maxV
    global visited
    if s == 0 or s < maxV:
        return
    if x == N:
        if s > maxV:
            maxV = s
            return
    for k in range(N):
        print(visited)
        if visited[k] == 0:
            visited[k] = 1
            dfs(x+1, s*(arr[x][k])*0.01)
            visited[k] = 0          # 행이 겹치지 않게하는 장치

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    visited = [0]*N
    maxV = 0
    dfs(0,1)
    print("#{} {:.6f}".format(tc,maxV*100))