from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def input_data(m:int,n:int):
    tomato, queue = [], deque()
    not_tomato = 0
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] == 1:
                queue.append([i, j])
            elif row[j] == -1:
                not_tomato += 1
        tomato.append(row)
    return tomato, queue, not_tomato

def BFS(m,n,tomato,queue,not_tomato):
    visited = [[0] * m for _ in range(n)]
    for num in queue:
        visited[num[0]][num[1]] = 1
    while queue:
        x, y = queue.popleft()
        add = visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and not tomato[nx][ny]:
                visited[nx][ny] = (add + 1)
                queue.append([nx, ny])
    zero_visited = 0
    res = 0
    for row in visited:
        zero_visited += row.count(0)
        if res <= max(row):
            res = max(row)
    if zero_visited == not_tomato:
        return res - 1
    else:
        return -1

def BOJ7576():
    m,n = map(int,input().split())
    tomato, queue, not_tomato= input_data(m,n)
    print(BFS(m,n,tomato,queue,not_tomato))
BOJ7576()