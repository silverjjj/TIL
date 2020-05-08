# #2105. [모의 SW 역량테스트] 디저트 카페 - 백트래킹으로 품
# 큐로 풀려고 해봤는데 절대안됨..
dx = [1, 1, -1, -1] # k = 0 , 1 , 2 , 3 가자
dy = [1, -1, -1, 1] # 위치 우하,좌하,좌상,우상 기준방향은 시계방향
'''
4           
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
'''
def dessert(x,y,k,nums):
    global arrive_x,arrive_y ,rm
    # 범위 넘어가면 리턴
    if x >= n or y >= n or x < 0 or y < 0:
        return
    # k가 더커지면 리턴
    if k >= 4:
        return
    # 도착하면 리턴
    if k == 3 and arrive_x ==x and arrive_y ==y:
        print(len(nums))
        return

    if rm[x][y] in nums:
        # print(visit)
        return
    # 계속 한방향으로 ,nums+[rm[x][y]]
    dessert(x+dx[k],y+dy[k],k,nums+[rm[x][y]])
    # 계속 한방향으로 가다가 도저히 갈곳이 없다면, 꺾는 방향으로
    dessert(x+dx[k],y+dy[k],k+1,nums+[rm[x][y]])



n = int(input())
rm = [list(map(int,input().split())) for _ in range(n)]
maxV = 0
for i in range(0,n-1):
    for j in range(1,n-1):
        arrive_x = i
        arrive_y = j
        nums = []
        # print(i,j)
        dessert(i,j,0,nums)




# def dfs(x,y):
#     global maxV
#     use = [[0]*n for _ in range(n)]
#     visited = [0]*101
#     s = []
#     s.append([x,y])
#     visited[rm[x][y]] = 1
#     use[x][y] = 1
#     tmpx=tmpy=0
#     while s:
#         for row in use:
#             print(row)
#         print(tmpx,tmpy)
#         print("-------------------------")
#         # tmp는 전 위치의 좌표
#
#         sx,sy = s.pop(0)
#         t = use[sx][sy]
#         for k in range(4):
#             nx = sx + dx[k]
#             ny = sy + dy[k]
#             if 0<=nx<n and 0<=ny<n and visited[rm[nx][ny]] == 0:
#                 if tmpx != nx or tmpy != ny:
#                     s.append([nx, ny])
#                     use[nx][ny] = 1 + t
#                     visited[rm[nx][ny]] = 1
#                     if x == nx and y == ny:
#                         return
#
#         # 전위치를 tmp에 저장
#         tmpx,tmpy = sx,sy
#
#     # for row in use:
#     #     print(row)
#     print("한턴끝")


