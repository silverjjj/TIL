# 다익스트라
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
adj = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,w = map(int,input().split())
    adj[a].append([w,b])

start, end = map(int,input().split())
INF = float('inf')
weight = [INF] * (N+1)
weight[start] = 0
hq = []
heapq.heappush(hq,[0,start])
# print(adj)
while hq:
    w, cur = heapq.heappop(hq)
    for next_w, next_node in adj[cur]:
        if weight[next_node] > next_w + w:
            weight[next_node] = next_w + w
            heapq.heappush(hq,[next_w + w, next_node])
print(weight[end])