# # SWex5656. [모의 SW 역량테스트] 벽돌 깨기
import copy

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def after(rm):
    for j in range(W):
        tmp = []
        for i in range(H-1,-1,-1):
            if rm[i][j] != 0:
                tmp.append(rm[i][j])
                rm[i][j] = 0
        for k in range(H-1,H-1-len(tmp),-1):
            rm[k][j] = tmp.pop(0)

def drop(p,rm):
    # 중복순열 p가 들어온다.
    q = []
    for j in p:
        visit = [[0] * W for _ in range(H)]
        for i in range(H):
            # 0이 아닌곳에 부딪힌다.
            if rm[i][j] != 0:
                q.append([i,j])
                # rm[i][j] = 0
                while q:
                    # print(q)
                    x,y = q.pop(0)
                    # print(x,y,rm[x][y])
                    for l in range(0, rm[x][y]):
                    # while l <= rm[x][y]:
                        for k in range(4):
                            nx = x + dx[k]*l
                            ny = y + dy[k]*l
                            if 0<=nx<H and 0<=ny<W and rm[nx][ny] != 0 and visit[nx][ny] ==0:
                                if rm[nx][ny] == 1:
                                    visit[nx][ny] = 1
                                else:
                                    q.append([nx,ny])
                                    visit[nx][ny] = 1

                # 폭탄 터지는부분
                for i in range(H):
                    for j in range(W):
                        if visit[i][j] == 1:
                            rm[i][j] = 0
                after(rm)
                break


T = int(input())
for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    room = [list(map(int,input().split())) for _ in range(H)]
    maxV = 0
    # 중복 순열 만들기 W개중에서 N개를 가진 중복순열을 만든다.
    def perm(k):
        global maxV
        if N == k:
            rm = copy.deepcopy(room)
            drop(p, rm)
            cnt = result = 0
            for ro in rm:
                cnt += ro.count(0)
                # print(cnt)
            if cnt > maxV:
                maxV = cnt
        else:
            for i in range(len(arr)):
                p[k] = arr[i]
                perm(k + 1)
    arr = [number for number in range(W)]
    # print(arr)
    p = [0] * N
    perm(0)
    print("#{} {}".format(tc,W*H-maxV))
