dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def dfs(i,j):
    global visited
    stack = [[i,j]]
    visited[i][j] = 1
    while stack:
        x,y = stack.pop()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx<m and 0<=ny<n and mapping[nx][ny] and not visited[nx][ny]:
                stack.append([nx,ny])
                visited[nx][ny] = 1
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    else:
        land = []
        mapping = []
        for i in range(m):
            arr = list(map(int,input().split()))
            mapping.append(arr)
            for j in range(n):
                if arr[j] == 1:
                    land.append([i,j])
        cnt = 0
        visited = [[0] * n for _ in range(m)]
        for x,y in land:
            if not visited[x][y]:
                dfs(x,y)
                cnt += 1
        print(cnt)