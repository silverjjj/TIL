# #2105. [모의 SW 역량테스트] 디저트 카페
# def dfs(x,y):
#     global cnt
#     visit = [[0]*n for _ in range(n)]
#     dx = [-1,-1,1,1]
#     dy = [-1,1,1,-1]
#     c = ['a','b','c','d']
#     s = []
#     clist = []
#     rmlist = []
#     s.append([x,y])
#     rmlist.append(rm[x][y])
#     while s:
#         for row in visit:
#             print(row)
#         print('------------------')
#         # if x==nx and y == ny:
#         sx,sy = s.pop(0)
#         for k in range(4):
#             nx = sx + dx[k]
#             ny = sy + dy[k]
#             if 0<=nx<n and 0<=ny<n:
#                 # and visit[nx][ny] == 0:
#                 if rm[nx][ny] not in rmlist:
#                     s.append([nx,ny])
#                     clist.append(c[k])
#                     rmlist.append(rm[nx][ny])
#                     visit[nx][ny] = 1
#                     print([x,y],[nx,ny],rmlist)
#                     print('----------------')
#                     break
#         print(x,nx,y,ny)
#         if x == nx and y == ny:
#             print('통과')
#             a = clist.count('a')
#             b = clist.count('b')
#             c = clist.count('c')
#             d = clist.count('d')
#             if a == c and b == d:
#                 cnt += 1
#
# n = int(input())
# rm = [list(map(int,input().split())) for _ in range(n)]
#
# cnt = 0
# # for i in range(n):
# #     for j in range(n):
# i,j = 0,1
# dfs(i,j)
# print(cnt)