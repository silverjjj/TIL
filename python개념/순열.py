# 순열 코드
def f(n,k):
    if n == k:  # 다 채운거니까 p를 출력
        print(p)
        # p의 갯수가 A갯수!
        # -> 5! = 120개
    else:
        for i in range(k):
            if used[i] == 0:    # i번 원소가 사용되지 않았다면
                used[i] = 1     # 사용함으로 표시
                p[n] = A[i]
                f(n+1,k)        # n+1 원소결정
                used[i] = 0     # 다른 자리에서 사용하도록 풀어줌
A = [2,3,5]
used = [0]*len(A)
p = [0]*len(A)   # 채울 칸수
f(0,len(A))  # 0번칸부터 채울껀데 총 5개 란 ㅡ이미













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