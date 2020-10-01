
import sys
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,cheese,visited):
    q = [[x,y]]
    visited[x][y] = 1
    arr = []
    while q:
        x,y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <=nx<R+2 and 0<=ny<C+2:
                if visited[nx][ny]:
                    continue
                if not cheese[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                elif cheese[nx][ny] == 1:
                    arr.append([nx,ny])
                    visited[nx][ny] = 1
    return arr
R, C = map(int,input().split())
cheese = [[0 for _ in range(C+2)]]
for _ in range(R):
    cheese.append([0]+list(map(int, read().split()))+[0])
cheese.append([0 for _ in range(C+2)])
cnt = 0
while True:
    visited = [[0] * (C+2) for _ in range(R+2)]
    arr = bfs(0,0,cheese,visited)
    if len(arr) == 0:
        print(cnt)
        print(res)
        break
    else:
        res = len(arr)
    cnt += 1
    for i,j, in arr:
        cheese[i][j] = 0