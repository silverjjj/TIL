def DFS():
    for j in range(M):
        for i in range(N):
            y = j-i
            x = i
            if 0<=x<N and 0<=y<M:
                print(x,y)
                if 0 <= x+1 < N:
                    visited[x+1][y] = max(visited[x+1][y], visited[x][y] + arr[x+1][y])
                if 0 <= y+1 < M:
                    visited[x][y+1] = max(visited[x][y+1] , visited[x][y] + arr[x][y+1])
                if 0<= x+1 < N and 0 <= y + 1 < M:
                    visited[x+1][y + 1] = max(visited[x+1][y + 1], visited[x][y] + arr[x+1][y + 1])
    for r in visited:
        print(r)
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = arr[0][0]
DFS()
print(visited[-1][-1])