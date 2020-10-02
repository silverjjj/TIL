from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,visited,height,n,mapping):
    dq = deque([])
    dq.append([x,y])
    visited[x][y] = 1
    while dq:
        x,y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and mapping[nx][ny] > height:
                dq.append([nx,ny])
                visited[nx][ny] = 1
def BOJ2568():
    n = int(input())
    mapping = [list(map(int,input().split())) for _ in range(n)]
    height = 0
    maxV = 1
    while True:
        cnt = 0
        visited = [[0 for _ in range(n)] for _ in range(n)]
        height += 1
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and mapping[i][j] > height:   # 처음 : 1보다 클때
                    bfs(i,j,visited,height,n,mapping)
                    cnt += 1
        if cnt > maxV:
            maxV = cnt
        res = 0
        for row in visited:
            res += sum(row)
        if res == 0 or res == 1:
            break
    print(maxV)
BOJ2568()