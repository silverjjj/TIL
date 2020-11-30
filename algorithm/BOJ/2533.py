'''
4%에서 틀림
'''

import sys
from collections import deque
# sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def BFS(dq, depth):

    L = len(dq)
    if L == 0:
        return
    res[depth%2] += L
    for _ in range(L):
        cur = dq.popleft()
        for next in adj[cur]:
            dq.append(next)
    BFS(dq,depth+1)
    return res

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    adj[u].append(v)
res = [0,0]
dq = deque([7])
print(BFS(dq,0))

'''
5
1 5
2 5
3 5
4 5
'''