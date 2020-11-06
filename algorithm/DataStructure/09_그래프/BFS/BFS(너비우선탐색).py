'''
BFS
입력
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
출력
1 2 3 4 5 7 6
'''
def bfs(v):
    q = []
    visited = [0]*(V+1)
    q.append(v)
    visited[v] = 1
    while q:
        u = q.pop(0)
        print(u,end=" ")
        for w in adj[u]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1

V,E =map(int,input().split())
arr = list(map(int,input().split()))
# 인접리스트를 딕셔너리로 활용
adj = {i:[] for i in range(1,V+1)}
# print(adj)
for i in range(E):
    s,e = arr[2*i], arr[2*i+1]
    adj[s].append(e)
    adj[e].append(s)
bfs(1)