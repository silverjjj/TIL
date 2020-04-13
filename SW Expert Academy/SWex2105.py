# #2105. [모의 SW 역량테스트] 디저트 카페 - 백트래킹으로 품


dx = [1, 1, -1, -1] # k = 0 , 1 , 2 , 3 가자
dy = [1, -1, -1, 1]
def dfs(x,y,k):
    nx = x + dx[k]
    ny = y + dy[k]
    if k == 3:
        return

    else:
        dfs(nx,ny,k+1)


    # global cnt


    # visit = [[0]*n for _ in range(n)]
    # s = []
    # # clist = []
    # rmlist = []
    # s.append([x,y])
    # rmlist.append(rm[x][y])
    # visit[x][y] = 1
    # while s:
    #     # for row in visit:
    #     #     print(row)
    #     # print('------------------')
    #     # # if x==nx and y == ny:
    #
    #     sx,sy = s.pop()
    #     for a in range(4):
    #         nx = sx + dx[a]
    #         ny = sy + dy[a]
    #         if 0<=nx<n and 0<=ny<n:
    #             if rm[nx][ny] not in rmlist:
    #                 s.append([nx,ny])
    #                 # clist.append(c[k])
    #                 rmlist.append(rm[nx][ny])
    #                 visit[nx][ny] = 1
    #                 break
    #     print(x,nx,y,ny)
    #     if x == nx and y == ny:
    #         print('통과')
    #         a = clist.count('a')
    #         b = clist.count('b')
    #         c = clist.count('c')
    #         d = clist.count('d')
    #         if a == c and b == d:
    #             cnt += 1

n = int(input())
rm = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
for i in range(1,n-1):
    for j in range(1,n-1):
        dfs(i,j,0)
print(cnt)