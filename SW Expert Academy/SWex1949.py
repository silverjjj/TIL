# SWex1949. [모의 SW 역량테스트] 등산로 조성
'''
가장 큰수의 위치를 찾는다.
그 위치를 중심으로 상 하 좌 우 를 이동, 이땐 큐를 사용 그리고 이동중
값이 크거나 같을때 k범위내에서 지형을 깍을수있다. (k가 아무리 커도 현 위치의 -1크기로)
만약 옆에 1일경우 이것도 - 가능
'''
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# def BFS(x,y,flag,height):
#     global maxV
#     if height > maxV:
#         maxV = height
#     visit[x][y] = 1
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0:
#             if rm[x][y] > rm[nx][ny]:
#                 BFS(nx,ny,flag,height+1)
#             if flag:
#                 for k in range(1,K+1):
#                     rm[nx][ny] -= k
#                     if rm[x][y] > rm[nx][ny]:
#                         BFS(nx,ny,False,height+1)
#                     rm[nx][ny] +=k
#
#     # 4면에 갈곳이 없다면 다시 visit = 0 표시
#     visit[x][y] = 0
#
# T = int(input())
# for tc in range(1,T+1):
#     N,K = map(int,input().split())
#     rm = [list(map(int,input().split())) for _ in range(N)]
#     visit = [[0]*N for _ in range(N)]
#     maxV = 0
#     res = 0
#     # 가장 큰 높이를 알기위한 알고리즘
#     for i in rm:
#         if max(i) > res:
#             res = max(i)
#     # print(res)
#     # max를 찾아내는 반복문
#     qw = 0
#     for x in range(N):
#         for y in range(N):
#             if rm[x][y] == res:
#                 # visit = [[0] * N for _ in range(N)]
#                 BFS(x,y,True,1)
#
#     print(tc,maxV)


dx = [-1,0,1,0]
dy = [0,1,0,-1]


def bfs(x,y,height,flag):
    global maxV
    visited[x][y] = 1
    if height > maxV:
        maxV = height
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            if mapping[x][y] > mapping[nx][ny]:
                bfs(nx,ny,height+1,flag)
            elif flag:
                for i in range(1, K+1):
                    mapping[nx][ny] -= i
                    if mapping[x][y] > mapping[nx][ny]:
                        bfs(nx, ny, height + 1, False)
                    mapping[nx][ny] += i
    visited[x][y] = 0

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    mapping = [list(map(int,input().split())) for _ in range(N)]
    high = 0
    maxV = 0
    for row in mapping:
        if max(row) > high:
            high=max(row)
    result = 0
    for i in range(N):
        for j in range(N):
            if mapping[i][j] == high:
                visited = [[0]*N for _ in range(N)]
                bfs(i,j,1,True)
                if maxV > result:
                    result = maxV
    print("#{} {}".format(tc,result))