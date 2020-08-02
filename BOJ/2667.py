# 2667 단지 번호 붙이기
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]
def dfs(x,y):
    global visited,cnt
    cnt += 1
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and mapping[nx][ny] == 1:
            dfs(nx,ny)

n = int(input())
mapping = [list(map(int,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
total = 0
cnt_lst = []
for i in range(n):
    for j in range(n):
        if mapping[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i,j)
            total += 1
            cnt_lst.append(cnt)
print(total)
cnt_lst.sort()
for c in cnt_lst:
    print(c)