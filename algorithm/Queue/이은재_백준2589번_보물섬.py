# bfs를 이용 +

def bfs(x,y):
    global maxV
    visit = [[0]*m for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    q = []
    q.append((x,y))
    visit[x][y] = 1
    while q:
        x,y = q.pop(0)
        t = visit[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] ==0 and rm[nx][ny] == 'L':
                q.append((nx,ny))
                visit[nx][ny] = t + 1

    for row in visit:
        if max(row) > maxV:
            maxV = max(row)
            # print(maxV)
    return

n,m = map(int,input().split())
rm = [list(map(str,input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
maxV = 0
# for row in rm:
#     print(row)

for i in range(n):
    for j in range(m):
        if rm[i][j] == 'L':
            bfs(i,j)
print(maxV-1)
