import sys
from collections import deque
input = sys.stdin.readline

def DFS(weight):
    visited = [0 for _ in range(N + 1)]
    dq = deque([])
    dq.append(start_node)
    visited[start_node] = 1
    while dq:
        cur_node = dq.popleft()
        for node, w in adj[cur_node]:
            if not visited[node] and w >= weight:
                visited[node] = 1
                dq.append(node)
    return True if visited[end_node] else False

N,M =map(int,input().split())
adj = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append([b,c])
    adj[b].append([a,c])
start_node, end_node = map(int,input().split())
minV = 1
maxV = 1000000000
res = 0
while minV <= maxV:
    midV = (maxV + minV)//2
    if DFS(midV):
        res = midV
        minV = midV + 1
    else:
        maxV = midV - 1
print(res)