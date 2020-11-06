from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    adj = {i : [] for i in range(1,N+1)}
    visited = [0 for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)
    dq = deque([1])
    visited[1] = 1
    cnt = 0
    while sum(visited) != N:
        cur = dq.popleft()
        for next in adj[cur]:
            if not visited[next]:
                cnt += 1
                visited[next] = 1
                dq.append(next)
    print(cnt)