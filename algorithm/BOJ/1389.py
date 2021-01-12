
import sys
from collections import deque
input = sys.stdin.readline
def BFS(idx):
    global minV, number
    visited = [0] * (N+1)
    dq = deque([idx])
    visited[idx] = 1
    cnt,res = 0,0
    while dq:
        L = len(dq)
        cnt += 1
        for _ in range(L):
            cur = dq.popleft()
            for next in arr[cur]:
                if visited[next]:
                    continue
                visited[next] = 1
                dq.append(next)
                res += cnt
    if minV > res:
        minV = res
        number = idx

N, M =map(int,input().split())
arr = [[] for _ in range(N+1)]
minV = float('inf')
number = -1
for _ in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
for idx in range(1,N+1):
    BFS(idx)
print(number)