'''
boj 16234
'''
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def Move(x,y):
    global mapping, flag
    dq = deque([(x,y)])
    tmp = [(x,y)]
    while dq:
        sx, sy = dq.popleft()
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(mapping[sx][sy] - mapping[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
                    tmp.append((nx,ny))
    if len(tmp) > 1:
        flag = True
        res = sum([mapping[_x][_y] for _x,_y in tmp]) // len(tmp)
        for i,j in tmp:
            mapping[i][j] = res


N,L,R = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                Move(i,j)
    if not flag:
        break
    cnt += 1
print(cnt)