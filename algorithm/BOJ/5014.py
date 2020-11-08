from collections import deque

def BFS(st):
    dq = deque([(st, 0)])
    visited = [0] * (F + 1)
    visited[st] = 1
    while dq:
        cur, cnt = dq.popleft()
        if cur == G:
            return cnt
        cnt += 1
        if 1<= cur + U <= F and not visited[cur + U]:
            dq.append((cur + U,cnt))
            visited[cur + U] = 1
        if 1<= cur - D <= F and not visited[cur - D]:
            dq.append((cur-D,cnt))
            visited[cur - D] = 1
    return 'use the stairs'

F,S,G,U,D = map(int,input().split())
print(BFS(S))