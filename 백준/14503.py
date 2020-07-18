# 14503_로봇청소기h

# 0:북, 1:동, 2:남, 3:서
# 왼 아래 오른 위
dx = [[0,1,0,-1], [-1,0,1,0] , [0,-1,0,1],  [1,0,-1,0]]
dy = [[-1,0,1,0], [0,-1,0,1] , [1,0,-1,0], [0,1,0,-1]]
diret = [3,0,1,2]
# 0:북, 1:동, 2:남, 3:서 을 기준으로 왼쪽을 의미함
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]

def find(x,y):
    global d, visited
    s = []
    s.append([x,y])
    visited[x][y] = 1
    while s:
        print(s)
        print("===========================")
        for row in visited:
            print(row)
        print("방향 ==> ",d)
        x, y = s.pop()
        nx = x + dx[d][0]
        ny = y + dy[d][0]
        # a 조건
        if visited[nx][ny] == 0 and mapping[nx][ny] == 0:
            print("1번")
            visited[nx][ny] = 1
            d = diret[d]
            # d = (d + 1) % 4  # 방향전환
            s.append([nx, ny])  # 이동
        # b조건: 칸(0)을 청소한경우
        elif visited[nx][ny] == 1 and mapping[nx][ny] == 0:
            print("2번")
            d = diret[d]
            # d = (d + 1) % 4  # 방향전환
            s.append([x,y])
        else:
            # 해당 위치가 벽 or 1바퀴를 다 돈경우
            tmp_cnt = 0
            for j in range(4):
                tmpx = x + dx[d][j]
                tmpy = y + dy[d][j]
                # tmpx = x + tmpdx[d][j]
                # tmpy = y + tmpdy[d][j]
                if visited[tmpx][tmpy] == 1:
                    tmp_cnt += 1

            if mapping[nx][ny] == 1 or tmp_cnt == 4:
                print("3번")
                d = d
                # 후진
                x_back = x + dx[d][1]
                y_back = y + dy[d][1]
                # 후진위치가 벽이면 함수 종료
                if mapping[x_back][y_back] == 1:
                    return
                # 아니면 해당 위치로 이동
                visited[x_back][y_back] = 1
                s.append([x_back,y_back])

N,M = map(int,input().split())
r,c,d = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# # 벽을 모두 8로 변경
# mapping[0][:] = [8]*M
# mapping[-1][:] = [8]*M
# # mapping[N-1] = 8
# for i in range(N):
#     mapping[i][0] = 8
#     mapping[i][M-1] = 8

find(r,c)
# for row in mapping:
#     print(row)
# print("===========================")
# for row in visited:
#     print(row)


