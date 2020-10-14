import sys
input = sys.stdin.readline

shape1 = [[(0,0),(1,0),(2,0),(2,1)], [(0,0),(0,1),(0,2),(-1,2)], [(0,0),(0,-1),(0,-2),(1,-2)],[(0,0),(-1,0),(-2,0),(-2,-1)]]
shape2 = [[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)]]
shape3 = [[(0,0),(0,1),(1,0),(1,1)]]
shape4 = [[(0,0),(1,0),(1,1),(2,1)],[(0,0),(0,1),(-1,1),(-1,2)],[(0,0),(-1,0),(-1,-1),(-2,-1)],[(0,0),(0,-1),(1,-1),(1,-2)]]
shape5 = [[(0,0),(0,-1),(0,1),(-1,0)],[(0,0),(0,1),(1,0),(-1,0)],[(0,0),(1,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0),(0,-1)]]
shapes = [shape1, shape2, shape3, shape4, shape5]
N,M = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
maxV = 0
for shape in shapes:

for x in range(N):
    for y in range(M):  # 시작점
        for arr in shape:   # 4 방향
            res = 0
            flag = True
            for dx,dy in arr:
                if 0 <= x+dx < N and 0 <= y+dy < M:
                    res += mapping[x+dx][y+dy]
                else:
                    flag = False
                    break
            if flag and res > maxV:
                maxV = res
print(maxV)