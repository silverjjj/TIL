# https://www.acmicpc.net/problem/17142
import sys
from collections import deque
from itertools import combinations
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(visited,q):
    global empty
    l = len(q)
    cnt = 0
    while cnt < l:
        cnt += 1
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if not mapping[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                    empty += 1
                elif mapping[nx][ny] == 2:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    if empty == empty_space:
        return True
    return False

N, M = map(int,read().split())
mapping = [list(map(int,read().split())) for _ in range(N)]
total = N*N
tmp = 0
empty_space = 0
virus = []
block = 0
for i in range(N):
    for j in range(N):
        if mapping[i][j] == 0:
            empty_space += 1
        elif mapping[i][j] == 1:
            block += 1
        elif mapping[i][j] == 2:
            virus.append([i,j])

L = len(virus)
if (total-block) == L:      # 빈공간이 없는경우
    minV = 0
else:
    minV = 10000

comb = list(combinations(virus,M))
for row in comb:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque([])
    for i,j in row:
        visited[i][j] = 1
        q.append([i,j])
    res = 0
    empty = 0
    while True:
        if bfs(visited,q):
            res += 1
            if minV > res:
                minV = res
            break
        elif res >= minV:
            break
        else:
            res +=1
if minV == 10000:
    minV = -1
print(minV)
'''

11 2
1 1 0 1 1 1 1 1 0 1 1
1 1 2 1 1 1 1 1 2 1 1
0 1 2 1 1 1 0 1 2 1 1
0 1 0 1 1 1 0 1 0 1 1
0 0 2 0 0 1 0 0 2 0 0
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1


5 3
2 2 2 0 0
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
answer : 2

4 2
0 1 1 0
2 1 1 2
2 1 1 2
0 1 1 0
answer : 2

5 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
2 0 0 2 0
1 1 1 1 1
answer : 2
'''