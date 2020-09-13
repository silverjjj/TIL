from collections import deque
def BFS(N,K):
    q = deque([N])
    maxV = 100001
    visited = [False] * maxV
    cnt = 0
    while q:
        n = len(q)
        for _ in range(n):
            cur = q.popleft()
            if not visited[cur]:
                visited[cur] = True
                if cur == K:
                    # print(cnt)
                    return cnt
                num1 = cur - 1
                num2 = cur + 1
                num3 = 2 * cur
                if 0 <= num1 < maxV:
                    q.append(num1)
                if 0 <= num2 < maxV:
                    q.append(num2)
                if 0 <= num3 < maxV:
                    q.append(num3)
        cnt += 1

N,K = map(int,input().split())
res = BFS(N,K)
print(res)
# print('끝')