# BOJ 2583번
# 스택
m,n,k = map(int,input().split())
arr= [[0]*n for _ in range(m)]
# print(arr)
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[j][i] = 1
def dfs(x,y):
    global cnt
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    nx = x
    ny = y
    s = []
    visit[nx][ny] = 1
    s.append([nx,ny])
    while s:
        x,y = s.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<m and 0<=ny<n and visit[nx][ny] ==0 and arr[nx][ny] == 0:
                s.append([nx,ny])
                visit[nx][ny] = 1
                cnt +=1

visit = [[0]*n for _ in range(m)]
area = 0
cnt_list = []
for i in range(m): # m=5 세로
    for j in range(n): # n = 7 가로
        if arr[i][j] == 0 and visit[i][j] == 0:
            cnt = 1
            dfs(i,j)
            area += 1
            cnt_list.append(cnt)
print(area)
cnt_list.sort()
for l in cnt_list:
    print(l, end = " ")
