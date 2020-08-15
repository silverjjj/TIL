# 11403 경로찾기
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
adj = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            adj[i+1].append(j+1)
# print(adj)
# res = [[0]*(n+1) for _ in range(n+1)]
q = []
for x in range(1, n+1):
    used = [0]*(n+1)
    q.append(x)
    while q:
        v = q.pop(0)
        for y in adj[v]:
            if not used[y]:
                used[y] = 1
                q.append(y)
    for num in used[1:]:
        print(num, end=" ")
    print()
