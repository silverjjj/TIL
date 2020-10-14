'''
M개의 나무
가장 처음에는 모든 칸에 양분이 5씩 존재
봄
나무는 자신의 나이만큼 양분을 먹고 나이가 1증가,
한칸에 여러개의 나무가 있으면 나이가 어린나무부터 양분 섭취,
자기 나이만큼 양분을 못먹으면 그 나무는 죽는다
여름
봄에 죽은 나무가 양분으로 변함
죽은나무 나이 % 2가 그 자리의 양분으로 추가
가을
나무가 번식함. 나무 나이는 5의 배수이면, 인접한 8칸에 나이가 1인 나무가 생김
겨울
s2d2가 땅을 돌아다니며 양분을 추가

k년후 땅에 살아있는 나무의 갯수를 구하자
'''
import sys
input = sys.stdin.readline
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
food_add = [list(map(int,input().split())) for _ in range(N)]
food = [[5 for _ in range(N)] for _ in range(N)]    # 양
tree = [[[] for _ in range(N)] for _ in range(N)]
trees = []
for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x][y].append(age)
    trees.append([x,y,age])
# for row in tree:
#     print(row)
# print("=====================")
# for row in food:
#     print(row)
# print("======================")
# 봄 and 여름
for _ in range(K):
    tmp = []
    print("여기")
    for r in tree:
        print(r)
    print('저기')
    for x,y,a in trees:
        print("x,y,a ==>", x,y,a)
        energy = food[x][y]         # 양분
        tree[x][y].sort()
        live_arr = []; death_arr = []
        print("양분 ==>",energy)
        print("나무 ==>",tree[x][y])
        for i in tree[x][y]:
            if (energy - i) >= 0:
                energy -= i
                tmp.append([x,y,i+1])        # 산 나무
                tree[x][y] = []
            else:
                death_arr.append(i//2)      # 죽은나무 => 양분
        print("산나무",live_arr)
        # 가을
        if len(tmp) >= 1:
            for x,y,age in tmp:
                if age % 5 == 0:
                    for k in range(8):
                        nx = x + dx[k]; ny = y + dy[k]
                        if 0<=nx<N and 0<=ny<N:
                            tmp.append([nx,ny,1])
                            tree[nx][ny] = []

        food[x][y] = energy + sum(death_arr)
    print("tmp==>",tmp)
    for x,y,age in tmp:
        tree[x][y].append(age)
    for i in range(N):
        for j in range(N):
            food[i][j] += food_add[i][j]
    trees = tmp[:]

    for row in tree:
        print(row)
    print("=====================")
    for row in food:
        print(row)
    print("=======================")