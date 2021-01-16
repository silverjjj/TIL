from collections import deque

def DFS():
    dq = deque([(0,0)])
    while dq:
        L = len(dq)
        for idx in range(L):
            x, y = dq.popleft()
            if 0 <= y + 1 < M:
                visited[x][y + 1] = max(visited[x][y + 1], visited[x][y] + arr[x][y + 1])
                if idx == 0:
                    dq.append((x, y + 1))
            if 0 <= x + 1 < N:
                visited[x + 1][y] = max(visited[x + 1][y], visited[x][y] + arr[x + 1][y])
                dq.append((x + 1, y))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = arr[0][0]
DFS()
print(visited[-1][-1])