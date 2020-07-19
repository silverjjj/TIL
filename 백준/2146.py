# 2146 다리만들기
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def divid(x,y):
    s = []
    s.append([x,y])
    coast_total = []
    coast_total.append([x, y])
    coast_tmp = []
    used[x][y] = 1
    mapping[x][y] += add
    while s:
        x,y = s.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and used[nx][ny] == 0 and mapping[nx][ny]:
                mapping[nx][ny] += add
                used[nx][ny] = 1
                s.append([nx,ny])
                coast_total.append([nx,ny])
    # 바다와 맞닿는 부분 찾기
    for i,j in coast_total:
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < n and 0 <= nj < n and mapping[ni][nj] == 0:
                coast_tmp.append([i,j])
                break
    return coast_tmp

def min_distance (x,y, current):
    global minV
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        d = visited[x][y]
        if d >= minV:
            return

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and mapping[nx][ny] != current:
                if mapping[nx][ny] == 0 and not visited[nx][ny] and not used[nx][ny]:
                    visited[nx][ny] = d + 1
                    q.append([nx, ny])
                # 다른 대륙에 도착하면
                elif used[nx][ny] and mapping[nx][ny] in continent:
                    minV = visited[x][y]
                    return
    return

n = int(input())
mapping = [list(map(int, input().split())) for _ in range(n)]
minV = 123456789
# step1. 땅 나누기
used = [[0]*n for _ in range(n)]
add = -1
coast = []
for i in range(n):
    for j in range(n):
        if mapping[i][j] and not used[i][j]:
            add += 1
            coast.append(divid(i,j))
continent = [num for num in range(1, len(coast)+1)]
# step2. 최단거리 찾기 (bfs 활용)
for arr in coast:
    for i,j in arr:
        visited = [[0] * n for _ in range(n)]
        min_distance(i,j,mapping[i][j])
print(minV)
