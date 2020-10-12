import sys,heapq

input = sys.stdin.readline
N,M = map(int,input().split())
adj = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append([c,b])
    # adj[b].append([c, a])

INF = float("inf")
weight = [INF] * (N+1)
weight[1] = 0
visited = [False] * (N+1)
hq = []
heapq.heappush(hq,[0,1])
while hq:
    w,cur = heapq.heappop(hq)
    print(w,cur)
    if visited[cur]:
        continue
    visited[cur] = True
    for next_w, next_node in adj[cur]:
        if weight[next_node] > next_w:
            weight[next_node] = next_w
            heapq.heappush(hq,[next_w, next_node])
    print(weight)
weight.pop(0)
print(sum(weight))
'''
4 5
2 4 5
2 3 2
1 3 3
3 4 5
1 2 1
'''