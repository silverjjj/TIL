import sys
from collections import deque
input = sys.stdin.readline

def BOJ10451():
    N = int(input())
    arr = [0]+list(map(int,input().split()))
    adj = {i : [] for i in range(1,N+1)}
    visited = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        adj[i].append(arr[i])
    dq = deque([])
    res = 0
    for j in range(1, N+1):
        if visited[j]:
            continue
        dq.append(j)
        while dq:
            cur = dq.popleft()
            for num in adj[cur]:
                if not visited[num]:
                    visited[num] = 1
                    dq.append(num)
        res += 1
    print(res)

for _ in range(int(input())):
    BOJ10451()