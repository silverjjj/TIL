def find(n, end):   # n = 1, end = 6
    visited = [0]*(V+1)
    s = []
    s.append(n)
    visited[n] = 1
    while s:
        n = s.pop()
        if n == end:
            return 1
        for j in range(1,V+1):
            if adj[n][j] == 1 and visited[j] ==0:
                s.append(j)
                visited[j] = 1
    return 0


T = int(input())
for tc in range(1,T+1):
    V, E = list(map(int,input().split()))
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        y,x = list(map(int,input().split()))
        adj[y][x] = 1
    # for row in adj:
    #     print(row)
    v,e = list(map(int,input().split()))
    find(v,e)
    print("#{} {}".format(tc,find(v,e)))