'''
백준 10026

'''
from collections import deque
d = ([0,1],[0,-1],[1,0],[-1,0])

def BFSforNormal(x,y):
    dq = deque([])
    dq.append([x,y])
    normal[x][y] = 1
    while dq:
        sx,sy = dq.popleft()
        for dx,dy in d:
            nx = sx +dx
            ny = sy + dy
            if 0<=nx<N and 0<=ny<N and not normal[nx][ny]:
                if colors[sx][sy] == colors[nx][ny]:
                    dq.append([nx,ny])
                    normal[nx][ny] = 1

def BFSforUnnormal(x,y):
    dq = deque([])
    dq.append([x,y])
    unnormal[x][y] = 1
    while dq:
        sx,sy = dq.popleft()
        for dx,dy in d:
            nx = sx +dx
            ny = sy + dy
            if 0<=nx<N and 0<=ny<N and not unnormal[nx][ny]:
                if colors[sx][sy] in ['R','G']:
                    if colors[nx][ny] in ['R','G']:
                        dq.append([nx, ny])
                        unnormal[nx][ny] = 1

                else:
                    if colors[sx][sy] == colors[nx][ny]:
                        dq.append([nx, ny])
                        unnormal[nx][ny] = 1


N = int(input())
colors = [list(map(str,input())) for _ in range(N)]
normal = [[0]*N for _ in range(N)]
unnormal = [[0]*N for _ in range(N)]
a,b = 0,0
for i in range(N):
    for j in range(N):
        if not normal[i][j]:
            BFSforNormal(i,j)
            a+=1
        if not unnormal[i][j]:
            BFSforUnnormal(i, j)
            b+=1
print(a,b)