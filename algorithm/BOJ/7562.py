'''
BOJ 7562
'''
from collections import deque
import sys
input = sys.stdin.readline
d = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))

def BFS(st_x,st_y):
    dq = deque([[st_x,st_y,0]])
    visited[st_x][st_y] = 1
    while dq:
        sx,sy,cnt = dq.popleft()
        if sx == end_x and sy == end_y:
            return cnt
        for dx,dy in d:
            nx = sx + dx
            ny = sy + dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                dq.append([nx,ny,cnt+1])
                visited[nx][ny] = 1
T = int(input())
for _ in range(T):
    N = int(input())
    st_x,st_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    visited = [[0] * N for _ in range(N)]
    print(BFS(st_x,st_y))