from collections import deque
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def dfs(x,y):
    q = deque([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx<m and 0<=ny<n and mapping[nx][ny] and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = 1

n,m = map(int,input().split())
if n == 0 or m == 0:
    pass
else:
    mapping = [list(map(int,input().split())) for _ in range(m)]
    cnt = 0
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mapping[i][j] and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)