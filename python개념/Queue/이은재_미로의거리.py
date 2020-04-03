# SWex5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
# queue + bfs
'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''
def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    visit = [[0]*n for _ in range(n)]
    # print(visit)
    q = []
    visit[x][y] = 1
    q.append((x,y))
    while q:
        # print(q)
        x,y = q.pop(0)
        t = visit[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0 and rm[nx][ny] ==0:
                q.append((nx,ny))
                visit[nx][ny] = t + 1
            elif 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0 and rm[nx][ny] ==3:
                # for row in visit:
                #     print(row)
                return t - 1
    # for row in visit:
    #     print(row)
    return 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [list(map(int,input())) for _ in range(n)]
    for row in rm:
        print(row)
    for i in range(n):
        for j in range(n):
            if rm[i][j] == 2:
                print("#{} {}".format(tc,bfs(i,j)))
