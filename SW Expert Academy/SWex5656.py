# SWex5656. [모의 SW 역량테스트] 벽돌 깨기
import itertools

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def after(rm):
    for row in rm:
        print(row)
    print('-------------------------------')

    for j in range(W):
        for i in range(H-1,1,-1):
            if rm[i][j] == 0:
                rm[i][j],rm[i-1][j] = rm[i-1][j],rm[i][j]



def drop(p):
    print(p)
    s = []
    for j in p:
        for i in range(H):
            # 0이 아닌곳에 부딪힌다.
            if rm[i][j] !=0:
                s.append([i,j])
                # rm[i][j] = 0
                while s:
                    x,y = s.pop()
                    for l in range(0, rm[i][j]):
                        for k in range(4):
                            nx = x + dx[k]*l
                            ny = y + dy[k]*l
                            if 0<=nx<H and 0<=ny<W and rm[nx][ny] !=0:
                                s.append([nx,ny])
                                print(s,rm[nx][ny])
                                rm[nx][ny] = 0

                break
    after(rm)


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
