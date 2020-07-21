n = int(input())
num = []
arr = [input() for _ in range(n)]
print(arr)
dx = [-1,1,0,0]
dy = [0,0,1,-1]
s = []
cnt = 0
for num in range(2):
    if num == 1:
        for a in range(n):
            for b in range(n):
                if arr[a][b] == 'G':
                    arr[a][b] = 'R'
    visited = [[0] * n for _ in range(n)]
    s = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                s.append([i, j])
                alp = arr[i][j]
                cnt += 1
                visited[i][j] = 1
                while s:
                    x,y = s.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and alp == arr[nx][ny]:
                            visited[nx][ny] = 1
                            s.append([nx,ny])
    print(cnt)