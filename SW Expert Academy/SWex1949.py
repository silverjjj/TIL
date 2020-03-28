# SWex1949. [모의 SW 역량테스트] 등산로 조성


def dfs(x,y):
    global rm,maxV,cnt,k
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    s = []
    s.append((x,y))
    while s:
        print(s)
        if rm[x][y] ==1 or rm[x][y] == 1-k:
            maxV = cnt
            cnt = 0
            s.pop()
        sx,sy = s.pop()
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0<=nx<n and 0<=ny<n:
                # for j in range(k):
                if rm[sx][sy] > rm[nx][ny]-k:
                    s.append((nx,ny))
                    cnt +=1


n,k = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]
maxV = 0
cnt = 1
# 가장 큰 높이를 알기위한 알고리즘
for i in range(n):
    for j in range(n):
        if rm[i][j] > maxV:
            maxV = rm[i][j]
for x in range(n):
    for y in range(n):
        if rm[x][y] == maxV:
            dfs(x,y)
            print(cnt)
