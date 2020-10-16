'''
진행순서
궁수 3명 한칸에 1명궁수
1. 한턴마다 궁수는 한명의 적 공격, 모든 궁수가 동시공격(겹침 가능)
1-1 D이하인 적중에 가장 가깝고
1-2 여러명이면 가장 왼쪽 적 공격
2. 공격받은 적 제외
3. 궁수의 공격이 끝나면 적이 아래로 이동
4. 모든적이 격자판에서 제외되면 게임 종료

문제풀이
1. 조합으로 궁수가 위치할 모든 가능성을 찾은뒤, 위치시킨다.
2. 각각의 궁수들은 조건에 따라 적을 공격(동시공격)하여 적을 죽임
3. 적의 위치가 x,y => x-1,y로 or 한줄을 pop 시킴
'''
import sys, copy
input = sys.stdin.readline

def comb(M, r):
    global tr_list
    if r == 0:
        tr_list.append(tr[:])
        return
    if M < r:
        return
    tr[r-1] = tmp[M-1]
    comb(M-1,r-1)
    comb(M-1,r)

def SHOT(arr,N):
    res = 0
    for n in range(N,0,-1):
        enemy_death = []
        for i in arr:       # 궁수 3명
            shot_x = n      # 궁수 1명 위치
            shot_y = i
            minD = 1000000
            tmp = []
            for x in range(1, D + 1):
                for y in range(-D, D + 1):
                    if 0 <= shot_x - x < N and 0 <= shot_y - y < M and room2[shot_x - x][shot_y - y] == 1 and abs(x) + abs(y) <= D:
                        tmp.append([abs(x) + abs(y),shot_x - x,shot_y - y])

            tmp.sort(key = lambda x : (x[0],x[2]))
            if len(tmp) > 0:
                enemy_death.append([tmp[0][1], tmp[0][2]])
        for i,j in enemy_death:
            if room2[i][j]:
                res += 1
            room2[i][j] = 0
        room2.pop(-2)
    return res

N, M, D = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
room.append([0]*M)
tr = [0]*3
tmp = [i for i in range(M)]
tr_list = []

comb(M, 3)

maxV = 0
for arr in tr_list:
    room2 = copy.deepcopy(room)
    for i in arr:
        room2[N][int(i)] = 2

    res = SHOT(arr,N)
    if maxV < res:
        maxV = res

print(maxV)