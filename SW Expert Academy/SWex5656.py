# SWex5656. [모의 SW 역량테스트] 벽돌 깨기
import itertools

# 현재 수정해야할곳
# 벽돌 제거후 떨어지는부분 보완해야함 << 완전고쳐야함
# 그리고 순열은 누적도 0,0,0 이렇게 가능해야하는데 이런게 다빠져있는상태
dx = [0,1,0,-1]
dy = [1,0,-1,0]


def after(rm):
    # for row in rm:
    #     print(row)
    # print('-------------------------------')

    # 벽돌 떨어지는부분
    for j in range(W):
        tmp = []
        for i in range(H-1,0,-1):
            if rm[i][j] != 0:
                tmp.append(rm[i][j])
                rm[i][j] = 0
        # print(tmp)

        for k in range(H-1,H-1-len(tmp),-1):
            rm[k][j] = tmp.pop(0)
    #
    #
    # print("벽돌 떨어짐")
    # for row in rm:
    #     print(row)
    # print("떨어짐 완료")


def drop(p,rm):
    # print(p)
    s = []
    for j in p:
        visit = [[0] * W for _ in range(H)]
        # for row in visit:
        #     print(row)
        # print('-------------------------')
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
                # for row in visit:
                #     print(row)
                # print('방문자표시~')
                after(rm)
                break




N,W,H = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(H)]
# 순열로 때릴 경우의수
# W개중 3개를 고르자
use = [0]*W
for i in range(W):
    use[i] = i
# print(use)
minV = 123456789
permu = list(itertools.permutations(use,3))
# print(permu)

for p in permu:
    # print(p)
    rm = []

    # 하나의 p가 갈때마다 새로운 rm으로 가줘야하는데
    # 그렇게 하기 위해 계속해서 room을 이용해 rm을 만들어줌
    # 근데 한바퀴 돌때마다 room이 영향을 받아 값이 변함.
    for row in room:
        rm.append(row)

    print('---------------')
    drop(p,rm)
    for row in room:
        print(row)
    cnt = 0


    if minV > cnt:
        minV = cnt

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
