import sys
import heapq
read = sys.stdin.readline

V,E = map(int,read().split())
k = int(read())

adj = {i : [] for i in range(1,V+1)}
for _ in range(E):
    u,v,w = map(int, read().split())
    adj[u].append([w,v])

visited = [False] * (V+1)
INF = float('inf')
weight = [INF] * (V+1)
weight[k] = 0
hq = []
heapq.heappush(hq, [0,k])   # 현위치, 가중치
while hq:
    # print(hq,visited)
    w, node = heapq.heappop(hq)
    for next_w, next_node in adj[node]:
        if not visited[next_node] and weight[next_node] > w + next_w:
            weight[next_node] = w + next_w
            heapq.heappush(hq,[w + next_w, next_node])

for num in weight[1:]:
    print(num if num != INF else 'INF')


'''
6 7
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
3 6 5
'''