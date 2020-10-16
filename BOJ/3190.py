import sys
input = sys.stdin.readline

dx = [-1,0,1,0] # 상 우 하 좌
dy = [0,1,0,-1]
direction = {0:[3,1], 1:[0,2], 2:[1,3], 3:[2,0]}    # 각방향에 따른 L,R

N = int(input())
room = [[0]*N for _ in range(N)]
for _ in range(int(input())):
    i,j = map(int,input().split())
    room[i-1][j-1] = 1
direct = {}
for _ in range(int(input())):
    i, j = map(str, input().split())
    num = 0
    if j == 'D':
        num = 1
    direct[int(i)] = num
snak = [[0,0]]  # idx 0이 머리, 가장큰게 꼬리
room[0][0] = 2  # 뱀
cur_direction = 1
flag = True
cnt = 0
tmp = []
while flag:
    sx, sy = snak.pop(-1)
    cnt += 1
    nx = sx + dx[cur_direction]
    ny = sy + dy[cur_direction]
    if 0<= nx < N and 0<=ny<N and room[nx][ny] <= 1:
        if room[nx][ny] == 1:   # 사과o
            snak.append([sx, sy])
            snak.append([nx, ny])
            room[sx][sy] = 2
            room[nx][ny] = 2
        elif room[nx][ny] == 0: # 사과 x
            if len(snak) >= 1:
                i,j = snak.pop(0)
                room[i][j] = 0
                snak.append([sx, sy])
                room[sx][sy] = 2
            else:
                room[sx][sy] = 0
            snak.append([nx, ny])
            room[nx][ny] = 2

    else:
        flag = False

    if cnt in direct.keys():
        num = direct[cnt]
        cur_direction = direction[cur_direction][num]
print(cnt)