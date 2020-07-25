from collections import deque

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
# print(adj)

q = deque()
q.append(1)
visited[1] = True
cnt = 0
while q:
    start = q.popleft()
    for i in adj[start]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            cnt +=1
print(cnt)


