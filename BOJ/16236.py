import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def BFS():
    global cnt, shark, room, res
    fish = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    sx, sy, size, distance = shark[0]
    visited[sx][sy] = 1
    dq = deque([])
    dq.append([sx,sy])
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            cur = visited[x][y]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and size >=room[nx][ny]:
                    visited[nx][ny] = cur + 1
                    dq.append([nx,ny])
                    if 0 < room[nx][ny]<size:
                        fish.append([nx,ny,room[nx][ny],cur + 1])

        if len(fish) >= 1:
            cnt += 1
            fish.sort(key= lambda x:(x[3],x[0],x[1]))
            i, j, size2, distance2 = fish.pop(0)
            res += (distance2-1)
            room[i][j] = 9; room[sx][sy] = 0
            if size == cnt:
                shark = [[i, j, size+1,0]]
                cnt = 0
            else:
                shark = [[i, j, size, 0]]
            return True

    return False
N = int(input())
room = []
shark = []
for i in range(N):
    arr = list(map(int,input().split()))
    room.append(arr)
    if len(shark) == 0 and 9 in arr:
        shark.append([i, arr.index(9),2,0])
res = 0
cnt = 0
while True:
    if not BFS():
        break
print(res)
