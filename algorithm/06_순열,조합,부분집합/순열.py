# # 순열 코드
# # swap 방법
def perm(k):
    if n == k:
        # print(k)
        # print(a)
        arr.append(a[:])
        return
    else:
        for i in range(k,n):
            # print(i,k)
            a[i],a[k] = a[k],a[i]
            perm(k+1)
            # print("여기",k)
            a[i], a[k] = a[k], a[i]
    return arr
arr = []
a = [1,2,3,4,5]
n = len(a)
res = perm(0)
print(res[44])
# # visited을 이용한 방법
# def perm(k):
#     global cnt
#     cnt +=1
#     if n == k:  # 다 채운거니까 p를 출력
#         print(p,cnt)
#         return
#         # -> 5! = 120개
#     else:
#         for i in range(n):
#             if not used[i]:    # i번 원소가 사용되지 않았다면
#                 used[i] = 1     # 사용함으로 표시
#                 p[k] = arr[i]
#                 perm(k+1)        # n+1 원소결정
#                 used[i] = 0     # 다른 자리에서 사용하도록 풀어줌
#
# arr = [1,2,3,4,5]
#
# cnt = 0
# n = len(arr)
# used = [0]*n
# p = [0]*n   # 결과저장배열
#       # 원소의 갯수
# perm(0)

print("========================================================")
# # 중복순열 코드
# def perm(n,cnt):
#     if n == K:  # 다 채운거니까 p를 출력
#         print(P,cnt)
#         return
#         # -> 5! = 120개
#     else:
#         for i in range(K):
#             P[n] = arry[i]
#             perm(n+1,cnt+1)        # n+1 원소결정
#
# arry = [1,2,3,4,5,6]
#
# K = len(arry)
# P = [0]*len(arry)   # 결과저장배열
#       # 원소의 갯수
# perm(0,0)





# def permutations(prefix,k):
#     if len(prefix) == r:
#         yield prefix
#     else:
#         for i in range(k,len(arr)):
#             arr[i], arr[k] = arr[k], arr[i]
#             for next in permutations(prefix + [arr[k]], k+1):
#                 yield next
#             arr[i], arr[k] = arr[k], arr[i]
#
# arr = [1,2,3,4,5]
# r = 3
# for perm in permutations([],0):
#     print(perm)