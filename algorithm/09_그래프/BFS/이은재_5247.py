from collections import deque
numbers = [1, -1, 2, -10]
def BFS():
    global result
    while Q:
        # print(Q)
        num, cnt = Q.popleft()
        if num == end:
            result = cnt
            return

        for obj in numbers:
            num2 = 0
            if obj == 1:
                num2 = num + 1
                if 0 < num2 <= 1000000 and visited[num2] != tc: # visited[num2] 자리에 있으면 append x
                    Q.append((num2,cnt+1))
                    visited[num2] = tc

            elif obj == -1:
                num2 = num - 1
                if 0 < num2 <= 1000000 and visited[num2] != tc:
                    Q.append((num2, cnt + 1))
                    visited[num2] = tc

            elif obj == 2:
                num2 = num * 2
                if 0 < num2 <= 1000000 and visited[num2] != tc:
                    Q.append((num2, cnt + 1))
                    visited[num2] = tc

            elif obj == -10:
                num2 = num - 10
                if 0 < num2 <= 1000000 and visited[num2] != tc:
                    Q.append((num2, cnt + 1))
                    visited[num2] = tc

T = int(input())
visited = [0] * 1000001
for tc in range(1, T+1):
    start, end = map(int,input().split())
    Q = deque()
    Q.append((start, 0))
    visited[start] = tc
    result = 0
    BFS()
    print("#{} {}".format(tc,result))