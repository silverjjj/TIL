# 1260 DFS와 BFS
def dfs(v):
    print(v, end=" ")
    visited[v] = 1
    tmp = sorted(arr[v])
    for num in tmp:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num)

def bfs(v):
    q = [v]
    visited2[v] = 1
    while q:
        # print(visited2,q)
        v = q.pop(0)
        print(v, end =" ")
        tmp = sorted(arr[v])
        for j in tmp:
            if visited2[j] == 0:
                q.append(j)
                visited2[j] = 1

N, M, V = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

visited = [0] * (N+1)
visited2 = [0] * (N+1)
dfs(V)
print()
bfs(V)