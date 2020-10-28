from collections import deque
def BFS(n):
    cnt = 0
    dq = deque([1, 2, 3])
    while dq:
        L = len(dq)
        for _ in range(L):
            cur = dq.popleft()
            for i in range(1,4):
                if cur + i > n:
                    continue
                elif cur + i == n:
                    cnt += 1
                else:
                    dq.append(cur + i)
    return cnt
T = int(input())
for _ in range(T):
    n = int(input())
    print(BFS(n))