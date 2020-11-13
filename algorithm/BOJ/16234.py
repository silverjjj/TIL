'''
4 시간 풀었는데 시간초과

1. 두나라의 인구차이가 L<= <=R 이면 국경선을 하루동안 연다
2. 열리면 "연합" 각칸의 인구수는  연합의 인구수 / 연합국 수, 소수점은 버림
3. 연합 해체, 국경선을 닫는다.
'''
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def MOVE():
    visited = [[0] * N for _ in range(N)]
    groups = {}
    idx = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                idx += 1
                visited[x][y] = idx
                dq = deque([])
                dq.append([x, y])
                tmp = [[x,y]]
                sum, cnt = mapping[x][y], 1
                while dq:
                    sx, sy = dq.popleft()
                    for k in range(4):
                        nx = sx + dx[k]
                        ny = sy + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and L <= abs(mapping[sx][sy] - mapping[nx][ny]) <= R:
                                visited[nx][ny] = idx
                                dq.append([nx, ny])
                                sum += mapping[nx][ny]
                                cnt += 1
                                tmp.append([nx,ny])
                if cnt != 1:
                    tmp.insert(0,[idx,sum//cnt])

    if not len(groups):
        return False
    return tmp

N,L,R = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
res = 0
flag = True
while flag:
    flag = MOVE()
    if not flag:
        break

    for i in range(1,len(flag)):
        for i, j in val[1]:
            mapping[i][j] = val[0]
    res += 1
print(res)




'''
2 10 20
0 30
50 10

2 10 20
0 20
50 20


4 1 9
96 93 74 30
60 90 65 96
5 27 17 98
10 41 46 20
correct: 1

(96,93,90)->93
(74,65)->69
(96,98)->97
(5,10)->7
(41,46)->43

/************/
5 1 5
88 27 34 84 9
40 91 11 30 81
2 88 65 26 75
75 66 16 14 28
89 10 5 30 75
correct: 1

(91,88)->89
(30,26)->28
(16,14)->15
(10,5)->7

4 10 50
10 100 80 90
30 100 70 70
40 50 60 140
50 20 100 10

'''