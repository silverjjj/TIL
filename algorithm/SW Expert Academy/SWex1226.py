# SWex1226 미로1
# 내가 자꾸 스택안쓰고 visited 으로만 풀려다가 꼬였음.
def f(x,y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    s = []
    s.append([x,y])
    visited[x][y] =1
    while len(s) > 0:
        ad = s.pop()
        for k in range(4):      # 4방향으로 ㄱㄱ
            nx = ad[0] + dx[k]
            ny = ad[1] + dy[k]
            # print(nx,ny)
            if miro[nx][ny] == 3:
                return "1"
            elif miro[nx][ny] == 0 and visited[nx][ny] == 0:
                s.append([nx,ny])
                visited[nx][ny] = 1
    return "0"

for tc in range(1,11):
    t = int(input())
    n = 100
    miro = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    print("#{} {}".format(tc,f(1,1)))
