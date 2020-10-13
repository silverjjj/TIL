'''
여러 연결 요소(connected componet)가 있을 수 있는지를 고려해야함
'''
import sys
from collections import deque
input = sys.stdin.readline

def BFS(q):
    # print("q -->", q)
    L = len(q)
    cnt = 0
    while cnt < L:
        cnt += 1
        cur_num, color = q.popleft()
        # print("cur_num, color ==>", cur_num, color)
        for next_num in adj[cur_num]:
            if not visited[next_num]:
                visited[next_num] = -color
                q.append((next_num, -color))
            elif visited[next_num] == color:
                return False
    return True
N = int(input())
for _ in range(N):
    V,E = map(int,input().split())
    adj = {i : [] for i in range(1,V+1)}
    for _ in range(E):
        x,y = map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)
    flag = True
    visited = [0] * (V + 1)
    q = deque([])
    for i in range(1, V+1):
        if visited[i]:
            continue
        q.append((i, 1))
        visited[i] = 1
        while q:
            if not BFS(q):
                flag = False
                break
        if not flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")
