# 2019 삼성코테 기출문제
# 백준_17472_다리만들기2
import heapq
dx = [-1,0,1,0]
dy = [0,1,0,-1]
N, M = map(int,input().split()) # x,y
room = [list(map(int,input().split())) for _ in range(N)]
# 군집 생성
used = [[0]*M for _ in range(N)]
group = []
for x in range(N):
    for y in range(M):
        s = []
        tmp = []
        if room[x][y] == 1 and used[x][y] == 0:
            s.append([x,y])
            tmp.append([x,y])
            while s:
                sx,sy = s.pop()
                used[sx][sy] = 1
                for l in range(4):
                    nx = sx + dx[l]
                    ny = sy + dy[l]
                    if 0<=nx<N and 0<=ny<M and used[nx][ny] == 0 and room[nx][ny] == 1:
                        used[nx][ny] = 1
                        s.append([nx,ny])
                        tmp.append([nx,ny])
            group.append(tmp[:])

# 군집간의 최단거리 측정
def find_distance(st_x,en_x,st_y,en_y):
    a = b = 0
    if st_x == en_x:
        if st_y > en_y:
            b = st_y
            a = en_y
        else:
            b = en_y
            a = st_y
        for y in range(a+1,b):
            if room[st_x][y] != 0:
                return False
        return True
    elif st_y == en_y:
        if st_x > en_x:
            b = st_x
            a = en_x
        else:
            b = en_x
            a = st_x
        for x in range(a+1,b):
            if room[x][st_y] != 0:
                return False
        return True
# 군집간의 최단거리를 찾자
n = len(group)  # 군집갯수
distance = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        minV = 11
        for st_x,st_y in group[i]:
            for en_x,en_y in group[j]:
                if st_x == en_x or st_y == en_y:
                    # 두 그룹 사이가 맞닿을경우 그 사이에 섬이 있냐 없냐?
                    if find_distance(st_x,en_x,st_y,en_y):
                        tmpD = abs(st_x-en_x)+abs(st_y-en_y)-1
                        if tmpD >= 2 and minV > tmpD :
                            minV = tmpD
        if minV != 11:
            distance[i][j] = minV
            distance[j][i] = minV

# 군집간 최단 거리를 담은 배열로 전체 최단 거리 측정
res = -1
# if flag:
INF = float("inf")
hq = []
weight = [INF] * n
visited = [0]*n
heapq.heappush(hq,(0,0))
while hq:
    wt, node = heapq.heappop(hq)
    if visited[node]:
        continue
    visited[node] = 1
    weight[node] = wt
    for j in range(n):
        if distance[node][j]:
            if weight[j] > distance[node][j]:
                weight[j] = distance[node][j]
                heapq.heappush(hq, (distance[node][j], j))
                distance[node][j] = distance[j][node] = 0
if sum(visited) == n:
    res = sum(weight)
print(res)


'''
3 10
1 1 0 0 0 0 0 0 1 1
1 0 0 0 0 1 0 0 0 1
0 0 1 0 0 0 1 0 1 1
output: 10
correct answer: -1

4 9
0 0 1 1 1 0 0 1 0
1 0 0 1 0 0 0 1 0
0 0 1 0 0 1 0 1 0
1 0 0 0 0 0 0 1 0
output: 12
correct answer: -1

'''