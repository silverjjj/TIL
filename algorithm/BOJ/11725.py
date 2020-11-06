from collections import deque
import sys
read = sys.stdin.readline
write = sys.stdout.write

def BOJ11725():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x,y = map(int, read().split())
        adj[x].append(y)
        adj[y].append(x)
    visited = [0 for _ in range(n+1)]
    q = deque()
    q.append(1)
    while q:
        cur = q.popleft()
        for num in adj[cur]:
            if not visited[num]:
                visited[num] = cur
                q.append(num)
    # print(visited)
    for number in visited[2:]:
        write("{}\n".format(number))
BOJ11725()