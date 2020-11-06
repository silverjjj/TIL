# 2178 미로탐색 bfs
from collections`import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        p = visited[x][y]
        if x == n-1 and y == m-1:
            return p

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and mapping[nx][ny] and not visited[nx][ny]:
                queue.append([nx,ny])
                visited[nx][ny] = p+1

n,m = map(int,input().split())
mapping = [list(map(int,input())) for _ in range(n)]
print(bfs(0,0))
