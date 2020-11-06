import sys
from collections import deque

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = visited[0][0][1] =1
    dq = deque([])
    dq.append([0,0,0])  #x,y, flag(0=> 벽뚫xx, 1 => 벽뚫 00)
    while dq:
        x,y,flag = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M:
                # 평지이고 방문한적 없을때
                if not mapping[nx][ny] and not visited[nx][ny][flag]:
                        visited[nx][ny][flag] = visited[x][y][flag] + 1
                        dq.append([nx,ny,flag])
                # 벽뚫 안했을때, 벽이 있으면 한번 뚫어서 이동해보자
                if not flag and mapping[nx][ny] and not visited[nx][ny][flag+1]:
                    visited[nx][ny][flag+1] = visited[x][y][flag] + 1
                    dq.append([nx,ny,1])
    return visited
N,M = map(int,input().split())
mapping = [list(map(int,input().strip())) for _ in range(N)]
visited = BFS()
minV = min(visited[N-1][M-1][0], visited[N-1][M-1][1])
maxV = max(visited[N-1][M-1][0], visited[N-1][M-1][1])
if minV == 0 and maxV == 0:
    print(-1)
elif minV == 0:
    print(maxV)
elif maxV == 0:
    print(minV)
else:
    print(minV)