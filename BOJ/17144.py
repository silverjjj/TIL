# 17144번 미세먼지 안녕!
'''
1. 청소기의 x위치를 찾는다.
2.
'''
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def Diffusion(room):
    for i in range(N):
        for j in range(M):
            if (not room[i][j] or mapping[i][j] == -1): # 미세먼지가 없거나 공기청정기
                continue
            tmp = []
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<M and mapping[nx][ny] != -1:
                    tmp.append([nx,ny,room[i][j]//5])
                    cnt += 1
            tmp.append([i,j,(room[i][j] - (room[i][j]//5)*cnt)])
            for x,y,w in tmp:
                room[x][y] += w
    return room[:]
N,M,T = map(int,input().split())
mapping = []
cleaner = []
for i in range(N):
    arr = list(map(int,input().split()))
    if -1 in arr:
        cleaner.append([i,0])
    mapping.append(arr)
cnt = 0
room = mapping[:]
print(room)
while cnt <= T:
    cnt += 1
    room = Diffusion(room)
    for row in room:
        print(row)
    print("=======================")
    for row in mapping:
        print(row)

# print(cleaner)
