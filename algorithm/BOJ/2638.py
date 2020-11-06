import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def Contack_Air():
    air = [[0 for _ in range(M)] for _ in range(N)]
    dq = deque([])
    dq.append([0,0])
    air[0][0] = 1

    while dq:
        x,y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]; ny = y + dy[k]
            if 0<=nx <N and 0<=ny<M and not room[nx][ny] and not air[nx][ny]:
                air[nx][ny] = 1
                dq.append([nx,ny])

    return air

def Melt_Cheese(air):
    global room, cheese
    melt_list = []      # 녹여야할 치즈 목록
    for x,y in cheese:
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and air[nx][ny]:
                cnt += 1
            if cnt >= 2:
                melt_list.append((x,y))
                break
    for i,j in melt_list:
        room[i][j] = 0
        cheese.remove((i,j))

N,M = map(int,input().split())
cheese = []
room = []
for i in range(N):
    tmp = list(map(int,input().split()))
    room.append(tmp[:])
    for j in range(M):
        if tmp[j] == 1:
            cheese.append((i,j))

time = 0
while True:
    Melt_Cheese(Contack_Air())
    time += 1
    if len(cheese) == 0:
        break
print(time)