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
tree_position = []
for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x][y].append(age)
    if (x, y) not in tree_position:
        tree_position.append((x,y))

# 봄 and 여름
live_arr = []; death_arr = []; tmp=[]
for x,y in tree_position:       # 나무의 위치
    energy = food[x][y]         # 양분
    live_tree = tree[x][y]       # 해당위치에 존재하는 모든 나무
    tree[x][y] = []
    live_tree.sort()
    for tr in live_tree:         # 나무에 양분을 줌
        if (energy - tr) >= 0:
            energy -= tr
            tree[x][y].append(tr + 1)
            live_arr.append([x,y,tr+1])
            if (x,y) not in tmp:
                tmp.append((x,y))        # 산 나무
                tree[x][y] = []
        else:
            death_arr.append(tr//2)      # 죽은나무 => 양분
    food[x][y] = energy

if len(live_arr) >= 1:  # 살아있는 나무가 존재할경우
    for x,y,age in live_arr:
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