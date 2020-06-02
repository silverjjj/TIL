# SWex1767. [SW Test 샘플문제] 프로세서 연결하기

'''
최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.
단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.

7
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
'''
dx = [-1,0,1,0] # 위 오 아래 왼
dy = [0,1,0,-1]
# new = [2,3,0,1]
# def dfs(s):
#     print("-----------------------------------------")
#     for row in visited:
#         print(row)
#     if s >= L:
#         print("도착")
#         return
#
#     # for num, lo in enumerate(semi_location):
#     #     if semi_used[num] == 1:
#     #         continue
#     x = semi_location[s][0]
#     y = semi_location[s][1]
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         flag = 0
#         if semi[nx][ny] != 1:
#             if k == 0:
#                 for i in range(0,nx+1):
#                     # print(semi[i][ny], visited[i][ny])
#                     if semi[i][ny] == 0 and visited[i][ny] == 0:
#                         continue
#                     flag = 1
#                     break
#             elif k == 1:
#                 for j in range(ny,N):
#                     if semi[nx][j] == 0 and visited[nx][j] == 0:
#                         continue
#                     flag = 1
#                     break
#             elif k == 2:
#                 for i in range(nx,N):
#                     if semi[i][ny] == 0 and visited[i][ny] == 0:
#                         continue
#                     flag = 1
#                     break
#             elif k == 3:
#                 for j in range(0,ny):
#                     if semi[nx][j] == 0 and visited[nx][j] == 0:
#                         continue
#                     flag = 1
#                     break
#             if flag == 0:
#                 while 0 <= nx < N and 0 <= ny < N:
#                     visited[nx][ny] = 1
#                     nx += dx[k]
#                     ny += dy[k]
#                 semi_used[s] = 1
#                 dfs(s+1)
#                 print(s,k,nx,ny)
#                 semi_used[s] = 0
#                 new_k = new[k]
#                 if new_k == 0:
#                     for i in range(nx,0,-1):
#                         if semi[i][ny] == 0:
#                             visited[i][ny] = 0
#                             continue
#                         break
#                 elif new_k == 1:
#                     for j in range(N-1, ny, -1):
#                         if semi[nx][j] == 0:
#                             visited[nx][j] = 0
#                             continue
#                         break
#                 elif new_k == 2:
#                     for i in range(N-1, nx, -1):
#                         if semi[i][ny] == 0:
#                             visited[i][ny] = 0
#                             continue
#                         break
#                 elif new_k == 3:
#                     for j in range(ny-1, 0, -1):
#                         if semi[nx][j] == 0:
#                             visited[nx][j] = 0
#                             continue
#                         break
#                 dfs(s+1)
# N = int(input())
# semi = [list(map(int,input().split())) for _ in range(N)]
# semi_location=[]
# for i in range(1,N-1):
#     for j in range(1,N-1):
#         if semi[i][j] == 1:
#             semi_location.append([i,j])
# print(semi_location)
# visited = [[0]*N for _ in range(N)]
# L = len(semi_location)
# semi_used = [0]*L
# dfs(0)




def dfs(k,total):
    if k >= n:
        return
    total_add = []
    if not semi_used[k]:
        semi_used[k] = 1
        x = semi_location[k][0]
        y = semi_location[k][1]
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            flag = True
            tmp = []
            if semi[nx][ny] != 1:
                if k == 0:
                    while 0<=nx<N and 0<=ny<N and flag:
                        if [nx,ny] not in total:
                            tmp.append([nx,ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False
                elif k == 1:
                    while 0<=nx<N and 0<=ny<N and flag:
                        if [nx,ny] not in total:
                            tmp.append([nx,ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False
                elif k == 2:
                    while 0 <= nx < N and 0 <= ny < N and flag:
                        if [nx, ny] not in total:
                            tmp.append([nx, ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False
                elif k == 3:
                    while 0<=nx<N and 0<=ny<N and flag:
                        if [nx,ny] not in total:
                            tmp.append([nx,ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False



N = int(input())
semi = [list(map(int,input().split())) for _ in range(N)]
semi_location=[]
for i in range(1,N-1):
    for j in range(1,N-1):
        if semi[i][j] == 1:
            semi_location.append([i,j])
n = len(semi_location)
semi_used = [0]*n
done = []
# print(False or False)
dfs(0,[])