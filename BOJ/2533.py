import sys
from collections import deque
input = sys.stdin.readline
def BFS(node):
    dq = deque([node])
    two = [1, 0]  # 홀 ,짝
    depth = 0
    while dq:
        L = len(dq)
        depth += 1
        cnt = 0
        for _ in range(L):
            cur = dq.popleft()
            if visited[cur]:
                continue
            visited[cur] = 1
            for next in dict[cur]:
                if not visited[next]:
                    cnt += 1
                    dq.append(next)
        two[depth % 2] += cnt
    return two
N = int(input())
dict = { i : [] for i in range(1,N+1)}
for _ in range(N-1):
    u,v = map(int,input().split())
    dict[u].append(v)
    dict[v].append(u)
visited = [0 for _ in range(N+1)]
res = [0,0]
for i in range(1, N+1):
    if not visited[i]:
        two = BFS(i)
        res[0] += two[0]
        res[1] += two[1]
print(min(res))

'''
5
1 5
2 5
3 5
4 5
'''