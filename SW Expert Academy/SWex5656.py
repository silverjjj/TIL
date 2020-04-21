# SWex5656. [모의 SW 역량테스트] 벽돌 깨기
import itertools

# 현재 수정해야할곳
# 벽돌 제거후 떨어지는부분 보완해야함 << 완전고쳐야함
# 그리고 순열은 누적도 0,0,0 이렇게 가능해야하는데 이런게 다빠져있는상태



dx = [0,1,0,-1]
dy = [1,0,-1,0]


def after(rm):
    for row in rm:
        print(row)
    print('-------------------------------')

    # 벽돌 떨어지는부분
    for j in range(W):
        for i in range(H-1,1,-1):
            if rm[i][j] != 0:
                while rm[i+1][j] != 0 or i+1 != H-1:
                    rm[i][j], rm[i + 1][j] = rm[i + 1][j], rm[i][j]


        #     if rm[i][j] != 0:
        #         tmp.append(rm[i][j])
        # rm[]
        #         rm[i][j],rm[i-1][j] = rm[i-1][j],rm[i][j]
    for row in rm:
        print(row)
    print('-------------------------------')


def drop(p):
    print(p)
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
                    print(x,y,rm[x][y])
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
                for row in visit:
                    print(row)
                print('방문자표시~')
                after(rm)
                break


def per():
    # permu = list(itertools.permutations(use,3))
    # print(permu)
    # for p in permu:
    p = [2,2,7]
    drop(p)
    for row in rm:
        print(row)

# rm 만드기
N,W,H = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(H)]


# 순열로 때릴 경우의수
# W개중 3개를 고르자
use = [0]*W
for i in range(W):
    use[i] = i
print(use)
per()

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
