# 1012 유기농배추
dx = [1,-1, 0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    s = []
    s.append([x,y])
    visited[x][y] = 1
    while s:
        x,y = s.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<m and 0<=ny<n and mappping[nx][ny] and not visited[nx][ny]:
                s.append([nx,ny])
                visited[nx][ny] = 1

N = int(input())
for _ in range(N):
    m,n,c = map(int,input().split())
    mappping = [[0]*n for _ in range(m)]
    visited = [[0]*n for _ in range(m)]
    for _ in range(c):
        x,y = map(int,input().split())
        mappping[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if mappping[i][j] and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)