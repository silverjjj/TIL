# SWex4871 그래프 경로 스택과 dfs 사용
def dfs(start, end):
    visited = [0] * (V + 1)
    s = []
    s.append(start)
    visited[start] = 1
    while s:
        # print(s)
        n = s.pop()
        visited[n] = 1
        if n == end:
            return 1
        for t in G[n]:
            if visited[t] == 0:
                s.append(t)
    return 0
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        v,e = map(int,input().split())
        G[v].append(e)
    v,e = map(int,input().split())
    print("#{} {}".format(tc, dfs(v,e)))