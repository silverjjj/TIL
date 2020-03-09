# SWex1226 미로1
def f(x,y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    sx = x
    sy = y
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if miro[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[sx][sy] = 1
                f(nx, ny)
                visited[sx][sy] = 0
                f(nx, ny)
            elif miro[nx][ny] == 3:
                return 1

for tc in range(1,11):
    t = int(input())
    miro = [list(map(int, input().split())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    result = 0
    # for row in miro:
    #     print(row)
    f(1,1)
    print("#{} {}".format(tc,result))