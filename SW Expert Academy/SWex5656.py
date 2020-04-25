# # SWex5656. [모의 SW 역량테스트] 벽돌 깨기
import itertools

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def after(rm):
    for j in range(W):
        tmp = []
        for i in range(H-1,0,-1):
            if rm[i][j] != 0:
                tmp.append(rm[i][j])
                rm[i][j] = 0
        for k in range(H-1,H-1-len(tmp),-1):
            rm[k][j] = tmp.pop(0)

def drop(p,rm):
    # 중복순열 p가 들어온다.
    s = []
    for j in p:
        visit = [[0] * W for _ in range(H)]
        for i in range(H):
            # 0이 아닌곳에 부딪힌다.
            if rm[i][j] !=0:
                s.append([i,j])
                # rm[i][j] = 0
                while s:
                    x,y = s.pop()
                    # print(x,y,rm[x][y])
                    for l in range(0, rm[x][y]):
                        for k in range(4):
                            nx = x + dx[k]*l
                            ny = y + dy[k]*l
                            if 0<=nx<H and 0<=ny<W and rm[nx][ny] != 0 and visit[nx][ny] ==0:
                                s.append([nx,ny])
                                # rm[nx][ny] = 0
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
    minV = 123456789
    # 중복 순열 만들기 W개중에서 N개를 가진 중복순열을 만든다.
    permu = list(itertools.product(range(W),repeat=N))
    for p in permu:
        rm = [[0] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                rm[i][j] = room[i][j]
        drop(p,rm)
        cnt = 0
        for ro in rm:
            for r in ro:
                if r != 0:
                    cnt +=1
        if minV > cnt:
            minV = cnt
    print("#{} {}".format(tc,minV))
'''
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
'''
