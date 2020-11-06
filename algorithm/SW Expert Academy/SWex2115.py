#
'''
8 3 12
9 1 6 7 5 4 6 7
9 5 1 8 8 3 5 8
5 2 6 8 6 9 2 1
9 2 1 8 7 5 2 3
6 5 5 1 4 5 7 2
1 7 1 8 1 9 5 5
6 2 2 9 2 5 1 4
7 1 1 2 5 9 5 7

4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7
'''

# def find(st,x,y):
#     print(x,y)
#
#     # pass
# n,m,maxc = map(int,input().split())
# rm = [list(map(int,input().split())) for _ in range(n)]
# # n*n에서 m개씩 일렬로 선택
# for i in range(n):
#     for j in range(n-m+1):
#         # print(rm[i][j:j+m])
#         find(j+m,i,0)
# # 선택할때마다 find 함수 ㄱ
#
# def subset(k, sum_num, total,comp):
#     global visited,maxV
#     if sum_num > maxc:  # 가지치기
#         return
#     if k == m:  # 목표도달
#         if sum_num <= maxc:
#             if comp > maxV:
#                 maxV = comp
#         return
#     else:
#         visited[k] = 1
#         subset(k + 1, sum_num + total[k], total,comp+(total[k]**2))
#         visited[k] = 0
#         subset(k + 1, sum_num, total, comp)
#
# def find(rm,c,st):
#     total = []
#     to = 0
#     if c == n:
#         return
#     for j in st:
#         # total.append(rm[c][j])
#         to += rm[c][j]
#     com = 0
#         # print(total)
#     if to <= maxc:
#         for l in st:
#             com += (rm[c][l]**2)
#     else: #  total > maxc:
#         subset(0,0,total,0)
#         com = maxV
#     print(com,maxc)
#     find(rm,c+1,st)


def subset(k, sum_num, total,comp):
    global visited,maxV
    if sum_num > maxc:  # 가지치기
        return
    if k == m:  # 목표도달
        if sum_num <= maxc:
            if comp > maxV:
                maxV = comp
        return
    else:
        visited[k] = 1
        subset(k + 1, sum_num + total[k], total,comp+(total[k]**2))
        visited[k] = 0
        subset(k + 1, sum_num, total, comp)


def find(x,y):
    global result
    if y+m < n:
        v = 0
        for l in range(y,n):
            v = sum(rm[x][l:l+m])
            com = 0
            if v <= maxc:
                for k in rm[x][l:l+m]:
                    com += (k**2)
            else: #  total > maxc:
                subset(0,0, rm[x][l:l+m])
                com = maxV


            result.append(v)
n,m,maxc = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]
result = []
stan = 0
for i in range(n):
    fos j in range(n-m+1):
        stan = rm[i][j:j+m]  # 기준값
        find(i,j+m+1) # 모든 같은행 찾기
        # last()      # 남은것

# print(st)
# for _ in range(n-1):
#     for j in range(m):
#         st[j]+=1
#     print(st)
#     find(rm,0,st)
# result = sorted(result)
# print(result)
# last = result[-1]+result[-2]
# print(last)
