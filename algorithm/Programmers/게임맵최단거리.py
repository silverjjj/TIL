from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        add = visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = (add + 1)
                q.append([nx,ny])
            if nx == n-1 and ny == m-1 and visited[nx][ny]:
                answer = visited[n-1][m-1]
                return answer
    return answer




maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1]]

print(solution(maps))