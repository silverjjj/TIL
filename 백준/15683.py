# # 15683_감시
# # 위 왼 아래 오른
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# direction = [[],
#              [[0],[1],[2],[3]],
#              [[0,2],[1,3]],
#              [[0,3],[3,2],[1,2],[0,1]],
#              [[0,1,3],[0,3,2],[1,2,3],[0,1,2]],
#              [[0,1,2,3]]]
#
# def dfs(i):
#     global visited, used, maxV
#     print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#     print(used)
#     if i == n:
#         print("===================================")
#         for row in visited:
#             print(row)
#
#     # for i in range(n):
#     #     if used[i] == 0:
#     #         used[i] = 1
#     x = cctv[i][0]
#     y = cctv[i][1]
#     cctv_type = cctv[i][2]
#     d = direction[cctv_type]
#     # visited에 cctv 감시 가능한 공간 표시
#     for num in d:
#         # num을 다 1로 표시하고 다음 위치로
#         tmp = []
#         print("num===>", num)
#         for l in num:
#             nx = x; ny = y
#             for j in range(maxV):
#                 nx += dx[l]
#                 ny += dy[l]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if room[nx][ny] == 6:
#                         break
#                     elif room[nx][ny] == 1 or room[nx][ny] == 0:
#                         visited[nx][ny] = 1
#                         tmp.append([nx,ny])
#                 else:
#                     break
#         print("1번 tmp ===>", tmp)
#         # 모두 표시하면 dfs로 한단계 아래로 이동
#         dfs(i+1)
#         # used[i] = 0
#         print("d와 cctv_type==>",d, cctv_type)
#         print("2번 tmp ===>", tmp,)
#         if cctv_type != 5:
#             for r,c in tmp:
#                 print("rc",r,c)
#                 visited[r][c] = 0
#         dfs(i-1)
#
#
#
#
# N,M = map(int,input().split())
# room = [list(map(int,input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# nums = [1,2,3,4,5]
# maxV = 0
# if N >= M:
#     maxV = N
# else:
#     maxV = M
# print(maxV)
# cctv = []
# barrier = []
# for i in range(N):
#     for j in range(M):
#         if room[i][j] in nums:
#             # x위치, y위치, cctv종류
#             cctv.append([i,j,room[i][j]])
#         elif room[i][j] == 6:
#             barrier.append([i,j])
#
# n = len(cctv)
# # print(n)
# used = [0] * n
# # print(cctv)
# # print(barrier)
# dfs(0)
#
