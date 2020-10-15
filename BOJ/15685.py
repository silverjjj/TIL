import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,-1,0,1]
adds = [(0,0),(1,0),(0,1),(1,1)]

def MAX(a, max_a):
    if a > max_a:
        return a
    return max_a

def MIN(a, min_a):
    if a < min_a:
        return a
    return min_a

N = int(input())
room = [[0]*101 for _ in range(101)]
max_x = max_y = 0
min_x = min_y = 101
for _ in range(N):
    x, y, d, g = map(int,input().split())
    max_x = MAX(x, max_x)
    min_x = MIN(x, min_x)
    max_y = MAX(y, max_y)
    min_y = MIN(y, min_y)
    s = [d]
    room[y][x] = 1
    for _ in range(g):
        for i in range(len(s)-1,-1,-1):
            s.append((s[i] + 1) % 4)
    nx = x
    ny = y
    for k in s:
        nx += dx[k]
        ny += dy[k]
        room[ny][nx] = 1
        max_x = MAX(nx, max_x)
        min_x = MIN(nx, min_x)
        max_y = MAX(ny, max_y)
        min_y = MIN(ny, min_y)
res = 0
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        flag = True
        for add in adds:
            nx = x + add[0]
            ny = y + add[1]
            if not room[ny][nx]:
                flag = False
                break
        if flag:
            res += 1
print(res)