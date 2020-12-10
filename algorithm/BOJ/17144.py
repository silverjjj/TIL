'''
boj 17144번 미세먼지 안녕!
'''
import sys
input = sys.stdin.readline

d = ((0,1),(-1,0),(0,-1),(1,0)) # 반시계
d_ = ((0,1),(1,0),(0,-1),(-1,0))

def Diffusion():
    for i in range(N):
        for j in range(M):
            mapping2[i][j] += mapping[i][j]
            if mapping[i][j] < 5:
                continue
            next = mapping[i][j] // 5
            cnt = 0
            for dx,dy in d:
                nx = i + dx
                ny = j + dy
                if 0<=nx<N and 0<=ny<M and mapping[nx][ny] != -1:
                    cnt += 1
                    mapping2[nx][ny] += next
            mapping2[i][j] -= (next*cnt)

def Rotate():
    x = cleaner[0]
    y = 1
    cur = mapping2[x][y]
    mapping2[x][y] = 0
    for dx, dy in d:
        while 0 <= x + dx < N and 0 <= y + dy < M and mapping[x+dx][y+dy] != -1:
            x += dx
            y += dy
            next = mapping2[x][y]
            mapping2[x][y] = cur
            cur = next

    x = cleaner[1]
    y = 1
    cur = mapping2[x][y]
    mapping2[x][y] = 0
    for dx, dy in d_:
        while 0 <= x + dx < N and 0 <= y + dy < M and mapping[x+dx][y+dy] != -1:
            x += dx
            y += dy
            next = mapping2[x][y]
            mapping2[x][y] = cur
            cur = next

N,M,T = map(int,input().split())
mapping = []    # 집
cleaner = []    # 청소기 위치
for i in range(N):
    arr = list(map(int,input().split()))
    if -1 in arr:
        cleaner.append(i)
    mapping.append(arr)
cleaner.sort()

for _ in range(T):
    mapping2 = [[0]*M for _ in range(N)]
    Diffusion()
    Rotate()
    mapping = mapping2.copy()
res = 2
for r in mapping:
    res += sum(r)
print(res)