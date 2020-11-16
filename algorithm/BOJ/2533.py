'''
4%에서 틀림
'''

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def BFS(dq,depth):
    L = len(dq)
    if L == 0:
        return
    res[depth%2] += L
    for _ in range(L):
        cur = dq.popleft()
        if visited[cur]:
            continue
        visited[cur] = 1
        for next in dict[cur]:
            if not visited[next]:
                dq.append(next)
    BFS(dq,depth+1)
    return res

N = int(input())
dict = { i : [] for i in range(1,N+1)}
for _ in range(N-1):
    u,v = map(int,input().split())
    dict[u].append(v)
    dict[v].append(u)
visited = [0 for _ in range(N+1)]
res = [0,0]
dq = deque([1])
print(min(BFS(dq,0)))

'''
5
1 5
2 5
3 5
4 5
'''