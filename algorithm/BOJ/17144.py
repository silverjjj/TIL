# 17144번 미세먼지 안녕!
'''
boj 17144번 미세먼지 안녕!
'''
import sys
input = sys.stdin.readline

d = ((0,1),(-1,0),(0,-1),(1,0)) # 반시계
d_ = ((0,1),(1,0),(0,-1),(-1,0))

def Diffusion():
    dusts = {}
    for i in range(N):
        for j in range(M):
            if dusts.get((i, j)) is None:
                dusts[(i, j)] = 0
            if mapping[i][j] == 0:
                continue
            elif mapping[i][j] == -1:
                dusts[(i,j)] -= 1
                continue
            dusts[(i,j)] += mapping[i][j]
            next = mapping[i][j] // 5
            cnt = 0
            for dx,dy in d:
                nx = i + dx
                ny = j + dy
                if 0<=nx<N and 0<=ny<M and mapping[nx][ny] >= 0:
                    cnt += 1
                    if dusts.get((nx,ny)) is None:
                        dusts[(nx, ny)] = next
                    else:
                        dusts[(nx,ny)] += next
            dusts[(i,j)] -= (next * cnt)
    for key, val in dusts.items():
        mapping[key[0]][key[1]] = val

def Rotate():
    dict = {}
    x = cleaner[0]
    y = 0
    mapping[x][y] = 0
    cur = mapping[x][y]
    for dx, dy in d:
        while 0 <= x + dx < N and 0 <= y + dy < M:
            x += dx
            y += dy
            next = mapping[x][y]
            dict[(x, y)] = cur
            cur = next

    x = cleaner[1]
    y = 0
    mapping[x][y] = 0
    cur = mapping[x][y]
    for dx, dy in d_:
        while 0 <= x + dx < N and 0 <= y + dy < M:
            x += dx
            y += dy
            next = mapping[x][y]
            dict[(x, y)] = cur
            cur = next

    for num in cleaner:
        dict[(num, 0)] = -1

    for key, val in dict.items():
        mapping[key[0]][key[1]] = val

N,M,T = map(int,input().split())
mapping = []    # 집
cleaner = []    # 청소기 위치
for i in range(N):
    arr = list(map(int,input().split()))
    if -1 in arr:
        cleaner.append(i)
    cleaner.sort()
    mapping.append(arr)

for _ in range(T):
    Diffusion()         # 미세먼지 확산
    Rotate()
res = 2
for r in mapping:
    res += sum(r)
print(res)