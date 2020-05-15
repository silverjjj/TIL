# #2115. [모의 SW 역량테스트] 벌꿀채취
# # a = [16,6,5,3,4,1,6,7,13,36,675]
# # a = sorted(a,reverse=True)
# # print(a)
# def dfs(x,y,n,k):
#     global used
#     if n == k:
#         for i in used:
#             if i == 1:
#
#         print(used)
#     else:
#         used[n] = 1
#         (x,y,n+1,k)
#         used[n] = 0
#         (x, y, n + 1, k)

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
'''
# n,m,c = map(int,input().split())
# rm = [list(map(int,input().split())) for _ in range(n)]
# total = []     # 가장 큰 두자리를 위한것
# used = [0]*m
# # n에서 m개
# arr = [num for num in range(n)]
# for i in range(n-m+1):
#     tmp=arr[i:i+m]
#     for x in range(n):  # 세로축
#         left = tmp[0]
#         right = tmp[-1]
#         if sum(rm[x][x+left:x+right+1]) > c:
            # 순열 코드
m = int(input())
def perm(k):
    if k == m:
        print(p)
    else:
        for i in range(m):
            if use[i] == 0:
                use[i] = 1
                p[i] = 1
                perm(k+1)
                # use[i] = 0
                use[i] = 0
p = [0]*m
use = [0]* m
perm(0)


            # def perm(n):
            #     if n == k:  # 다 채운거니까 p를 출력
            #         print(p)
            #         return
            #         # -> 5! = 120개
            #     else:
            #         for i in range(k):
            #             if not used[i]:  # i번 원소가 사용되지 않았다면
            #                 # print(used,p)
            #                 p[n] = arr[i]
            #                 perm(n + 1)  # n+1 원소결정
            # arr = [1, 2, 3, 4]
            # k = len(arr)
            # used = [0] * len(arr)
            # p = [0] * len(arr)  # 결과저장배열
            # # 원소의 갯수
            # perm(0)
            #








# for i in range(n):
#     for j in range(n-m+1):
#         if sum(rm[i][j:j + m]) == c or sum(rm[i][j:j+m]) >= c:
#             dfs(i,j,0,m)
#             for x in range(i,n):
#                 for y in range(j,n-m+1):
#                     if sum(rm[x][y:y + m]) == c or sum(rm[x][y:y + m]) >= c:
#
#         re = comp=0
#         # c와 같을경우
#         if sum(rm[i][j:j+m]) == c:
#             for k in rm[i][j:j+m]:
#                 re +=k**2
#             total.append(re)
#         elif sum(rm[i][j:j+m]) > c:
#             per(rm[i][j:j+m],0,m)
#
#             result = sorted(rm[i][j:j + m],reverse=True)
#             for k in result:
#                 comp += k
#                 if c > comp:
#                     re +=k**2
#             total.append(re)
# total.sort()
# print(total)