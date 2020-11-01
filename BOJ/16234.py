'''
1. 두나라의 인구차이가 L<= <=R 이면 국경선을 하루동안 연다
2. 열리면 "연합" 각칸의 인구수는  연합의 인구수 / 연합국 수, 소수점은 버림
3. 연합 해체, 국경선을 닫는다.
'''
import sys
from collections import deque

read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def count_move():
    global res, mapping
    visited = [[0] * N for _ in range(N)]
    groups = []
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                visited[x][y] = 1
                q = deque([])
                q.append([x, y])
                group = [[x, y]]
                while q:
                    # print(q)
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if R <= abs(mapping[x][y] - mapping[nx][ny]) <= C:
                                visited[nx][ny] = 1
                                q.append([nx, ny])
                                group.append([nx, ny])
                # print(group)
                if len(group) > 1:
                    groups.append(group)
    print(groups)
    if len(groups) >= 1:
        res += 1
        for tmp in groups:
            total = 0
            for i, j in tmp:
                total += mapping[i][j]
            for i, j in tmp:
                mapping[i][j] = total // len(tmp)
        return True
    else:
        return False
N,R,C = map(int,input().split())
mapping = [list(map(int,read().split())) for _ in range(N)]
res = 0
while True:
    if not count_move():
        for r in mapping:
            print(r)
        break
    for r in mapping:
        print(r)
print(res)



'''
2 10 20
0 30
50 10
'''