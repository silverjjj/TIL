import sys
input = sys.stdin.readline

d = [(0,1),(0,-1),(1,0),(-1,0)]
direction = [[(0,-1),(0,1),(-1,0)],[(0,-1),(0,1),(1,0)],[(-1,0),(1,0),(0,-1)],[(-1,0),(1,0),(0,1)]]
def DFS(x,y,depth,sum,visited):
    global maxV
    if depth == 3:
        maxV = max(maxV, sum)
        return

    for dx,dy in d:
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx,ny,depth+1,sum+mapping[nx][ny], visited)
            visited[nx][ny] = 0
def O_sum_find(i,j):
    global maxV
    for d1, d2, d3 in direction:  # ㅗ을 계산하기 위한 for문
        try:
            res = mapping[i][j] + mapping[i + d1[0]][j + d1[1]] + mapping[i + d2[0]][j + d2[1]] + mapping[i + d3[0]][j + d3[1]]
        except:
            res = 0
        maxV = max(maxV, res)

N, M = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
maxV = 0
for i in range(N):
    for j in range(M):  # 시작점
        visited[i][j] = 1
        DFS(i,j,0,mapping[i][j],visited)
        visited[i][j] = 0
        O_sum_find(i,j)

print(maxV)