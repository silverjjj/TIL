# # 16236 아기상어
#
# '''
# 1초에 상하좌우 한칸씩 이동
#
#
# 먹을게 없다 => 엄마상어한테 요청
#
# 4방면에
# 물고기 1마리 => 먹자
# 여러마리 => 가장 가까운 물고기
#             가장 가까운 물고기가 많다면 가장 위에있는 물고기, 그것도 많으면 가장왼쪽물고기
# 이동은 상어(크기: 2) 보다 같거나 작을때 가능하고
# 작은것만 먹을수 있음. 자신의 크기와 같은수의 물고기를 먹으면 크기 1 증가
# 2크기의 상어가 물고기 2마리 먹으면 크기 3으로 상승
# '''
#
#
# '''
#
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4
#
# 크기2
# 시간3
# 4 3 2 9
# 0 0 0 0
# 0 0 0 0
# 1 2 3 4
# 크기2
# 시간9
# 4 3 2 0
# 0 0 0 0
# 0 0 0 0
# 9 2 3 4
#
# 시간10
# 크기3
# 4 3 2 0
# 0 0 0 0
# 0 0 0 0
# 0 9 3 4
#
# 시간 14
# 4 3 9 0
# 0 0 0 0
# 0 0 0 0
# 0 0 3 4
# '''
# n = int(input())
# maps = [list(map(int,input().split())) for _ in range(n)]
# size = 2
# size_plus = 0
# for l in range(n):
#     if 9 not in maps[l]:
#         continue
#     x = l
#     y = maps[l].index(9)
#     total = [[] for _ in range(2*n-1)]
#     for i in range(n):
#         for j in range(n):
#             res = abs(x-i) + abs(y-j)
#             total[res].append([i,j])
#
#     for c in range(1,2*n-1):
#         tmp = []
#         for i,j in total[c]:
#             if size > maps[i][j]:
#                 tmp.append()
# # for row in total:
# #     print(row)