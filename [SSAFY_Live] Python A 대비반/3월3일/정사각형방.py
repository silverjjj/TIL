dx = [-1, 0, 1, 0]  # 위 오른 아래 왼
dy = [0, 1, 0, -1]

def f(x,y): #좌표 2개, k
    global cnt
    global max_cnt
    global visited
    visited[x][y] = 1  # 해당 위치 방문표시시          
    if max_cnt < cnt:
        max_cnt = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if case[nx][ny] - case[x][y] == 1:
                cnt +=1
                f(nx, ny)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    temp = 0
    point = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt = 1
                max_cnt = 0
                f(i,j)
                if max_cnt > temp:
                    temp = max_cnt
                    point = case[i][j]
                elif max_cnt == temp:
                    if point > case[i][j]:
                        point = case[i][j]
    print("#{} {} {}".format(tc,point,temp))