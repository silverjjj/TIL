# 2573 빙산
'''
1. 한바퀴 돌면서 0이 아닌 모든 좌표의 디테일을 구함
2. -해줄 [x, y, -크기]를 모아둔다, 모든 경우를 따져본뒤 계산
3. 빙산이 몇개인지 찾아본다.

문제가 뭘까 ?
1. deepcopy
2. 계속 시간초과 뜨니까, 재귀함수에 문제가 있나 ?

'''

from collections import deque
import sys
dx = [-1, 1, 0, 0]  # 상하우좌
dy = [0, 0, 1, -1]

def bfs(x,y):
    global ice
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        minus[(x, y)] = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if ice[nx][ny] == 0:    # 빙산이 없는경우 +1 해준다
                    minus[(x, y)] += 1
                elif ice[nx][ny] != 0 and visited[nx][ny] == 0:  # 빙산인데 방문하지 않을경우 append시켜줌
                    q.append([nx,ny])
                    visited[nx][ny] = 1
    return minus
n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
year = 0
stan = n*m
while True:
    # step1. 빙하가 없으면 바로 종료
    res = 0
    for row in ice:
        res += row.count(0)
    if res == stan:
        print(0)
        sys.exit()

    # step2. 빙산 조사 시작
    island = 0
    minus = dict()
    visited = [[0] * m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                island += 1
                print(minus)
                # 두덩어리가 되는 순간 year 출력후 종료
                if island == 2:
                    print(year)
                    sys.exit()
    print("=====================")
    for row in ice:
        print(row)

    # step3. 빙산 녹이기
    for key, value in minus.items():
        ice[key[0]][key[1]] -= value
        if ice[key[0]][key[1]] < 0:
            ice[key[0]][key[1]] = 0

    # step4. 빙산을 다 녹이고 난뒤 1년 추가
    year += 1

'''
5 7
0 0 0 0 0 0 0
0 3 3 2 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0
5 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 10 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
5 7
0 0 0 0 0 0 0
0 3 6 0 6 7 0
0 3 0 0 0 10 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
5 7
0 0 0 0 0 0 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
5 7
0 0 0 0 0 0 0
0 9 8 3 8 9 0
0 9 8 0 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
5 5
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
7 7
0 0 0 0 0 0 0
0 1 1 0 1 1 0
0 1 9 1 9 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0


0
0
1
2
0
0
5
0
3
'''