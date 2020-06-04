# SWex 1249. [S/W 문제해결 응용] 4일차 - 보급로 D4
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    global minV
    q = deque([])
    q.append([x,y])
    visited[x][y] = rm[x][y]
    while q:
        sx,sy = q.popleft()
        if sx == N - 1 and sy == N - 1:
            if minV > visited[N-1][N-1]:
                minV = visited[N-1][N-1]
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0<=nx<N and 0<=ny<N:
                tmpV = rm[nx][ny] + visited[sx][sy]
                if visited[nx][ny] == -1 or visited[nx][ny] > tmpV:
                    visited[nx][ny] = tmpV
                    q.append([nx, ny])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rm = [list(map(int,input())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    minV = 987654321
    bfs(0,0)
    # for row in visited:
    #     print(row)
    print("#{} {}".format(tc, minV))
