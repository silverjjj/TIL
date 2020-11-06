import sys
import heapq
def dijkstra(start):
    INF = float('inf')
    weight = [INF for _ in range(n+1)]
    weight[start] = 0
    hq = []
    heapq.heappush(hq,[0,start])    # 가중치, 시작점
    while hq:
        w,node = heapq.heappop(hq)
        for next_w, next_node in adj[node]:
            if weight[next_node] > w + next_w:
                weight[next_node] = w + next_w
                heapq.heappush(hq,[w + next_w, next_node])
    return weight

read = sys.stdin.readline
n = int(input())
adj = {i : [] for i in range(1,n+1)}
for _ in range(n-1):
    x,y,z = map(int,read().split())
    adj[x].append([z,y])
    adj[y].append([z,x])

arr = dijkstra(1)
print(max(dijkstra(arr.index(max(arr[1:])))[1:]))