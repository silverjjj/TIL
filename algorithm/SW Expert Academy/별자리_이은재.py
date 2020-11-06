dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
def star(x,y):
    global cnt
    s = []
    s.append((x,y))
    while s:
        sx, sy = s.pop()
        visit[sx][sy] = 1
        for k in range(8):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0 <= nx < 10 and 0 <= ny < 10 and visit[nx][ny] == 0 and rm[nx][ny] == 1 :
                visit[nx][ny] = 1
                s.append((nx, ny))
    cnt += 1
T = int(input())
for tc in range(1,T+1):
    rm = [list(map(int,input().split())) for _ in range(10)]
    visit = [[0]*10 for _ in range(10)]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if rm[i][j] == 1 and visit[i][j] ==0:
                star(i,j)

    print("#{} {}".format(tc,cnt))