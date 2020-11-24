from collections import deque
import sys
input = sys.stdin.readline

def BFS(i):
    dq = deque([i])
    depth = 0
    visited = [False] * (N + 1)
    visited[i] = True
    while dq:
        cur = dq.popleft()
        depth += 1
        for next in adj[cur]:
            if visited[next]:
                continue
            visited[next] = True
            dq.append(next)
    return depth

N,M = map(int,input().split())
adj = [[] for _ in range(N+1)]
counts = [0] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    adj[b].append(a)
maxV = 0

for i in range(1,N+1):
    cnt = BFS(i)
    counts[i] = cnt
    maxV = max(cnt, maxV)
for j in range(1,N+1):
    if counts[j] == maxV:
        print(j, end=" ")




'''

15 14
3 1
3 2
4 3
5 3
6 5
3 7
7 12
7 13
12 14
15 6
8 4
11 4
9 8
10 8
'''