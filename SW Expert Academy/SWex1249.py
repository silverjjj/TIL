dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    s = []
    s.append([x,y])
    while s:
        # print(s)
        sx,sy = s.pop()
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if nx == last_x and ny == last_y:
                    print("--")
                else:
                    s.append([nx,ny])

N = int(input())
rm = [list(map(int,input())) for _ in range(N)]
print(rm)
for row in rm:
    print(row)

last_x = last_y = N-1
dfs(0,0)