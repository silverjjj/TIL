def f(x, y):
    global ladder
    global visited
    dx = [0, 0, -1]  # 좌우상
    dy = [-1, 1, 0]
    nx = x
    ny = y
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 100 and 0 <= ny < 100:
            if visited[nx][ny] == 0 and ladder[nx][ny] == 1:
                visited[nx][ny] = 1
                f(nx, ny)
                if nx == 0:
                    y_list.append(ny)


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    y_list = []
    for i in range(100):
        if ladder[99][i] == 2:
            start = i
            break
    visited[99][start] = 1
    f(99, start)
    print("#{} {}".format(tc, y_list[0]))