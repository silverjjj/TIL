'''
prim으로 풀수있는 문제
각각의 노드에서 최소값을 더해나가면 된다.
'''
import sys,heapq
input = sys.stdin.readline
N, M = map(int,input().split())
adj = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append([c,b])
    adj[b].append([c, a])
# print(adj)
visited = [False] * (N+1)
hq,res,cnt = [],0,0
heapq.heappush(hq,[0,1])
while hq and N > cnt:
    w,cur = heapq.heappop(hq)
    if visited[cur]:
        continue
    res += w
    cnt += 1
    visited[cur] = True
    for arr in adj[cur]:
        heapq.heappush(hq, arr)
print(res)
'''
4 5
2 4 5
2 3 2
1 3 3
3 4 5
1 2 1

4 3
2 4 5
2 3 2
3 4 5

'''