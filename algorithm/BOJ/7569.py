# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
read = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]
dh = [-1,1]
def bfs(q):
    cnt = 0
    l = len(q)
    while cnt < l:
        cnt += 1
        x, y, h = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and dict[h][nx][ny] == 0:
                dict[h][nx][ny] = 1
                q.append((nx, ny, h))
        for k2 in range(2):
            nh = h + dh[k2]
            if 1 <= nh < H + 1 and dict[nh][x][y] == 0:
                dict[nh][x][y] = 1
                q.append((x, y, nh))
    if len(q) == 0:
        return False
    return True

def findzero(dict,res):
    for h in range(1, H + 1):
        for row in dict[h]:
            for r in row:
                if r == 0:
                    return -1
    return res

M, N, H = map(int,read().split())
q = deque([])
dict = {}
for h in range(1,H+1):
    dict[h] = []
    for i in range(N):
        arr = list(map(int,read().split()))
        dict[h].append(arr)
        for j in range(M):
            if arr[j] == 1:
                q.append((i,j,h))
res = 0
while True:
    if not bfs(q):
        ans = findzero(dict,res)
        break
    res += 1
print(ans)