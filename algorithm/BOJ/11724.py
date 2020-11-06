# 11724 연결 요소의 개수
import sys
from collections import deque

def bfs(num):
    queue = deque()
    queue.append(num)
    while queue:
        x = queue.popleft()
        visited.add(x)
        for j in arr[x]:
            if j not in visited:
                visited.add(j)
                queue.append(j)

    return 1
n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    # map(int,sys.stdin.readline().split()) 은 input 입력보다 더 빠르게 입력이 가능
    x, y = map(int,sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

visited = set()
cnt = 0
for i in range(1, n+1):
    if i not in visited:
        visited.add(i)
        cnt += bfs(i)
print(cnt)