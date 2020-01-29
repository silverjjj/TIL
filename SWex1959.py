M = map(int, input().split())
N = map(int, input().split())
result1, result2 = 0, 0
if len(str(N)) > len(str(M)):
    for i in range(0,len(str(N))):
        result1 += len(str(N))[i] * len(str(M))[i]
        result2 += len(str(N))[-1-i] * len(str(M))[-1-i]
        if result1 > result2:
            print(result1)
        else:
            print(result2)
elif len(str(N)) < len(str(M)):
    for j in range(0,len(str(M))):
        result1 += len(str(N))[j] * len(str(M))[j]
        result2 += len(str(N))[-1 - j] * len(str(M))[-1 - j]
        if result1 > result2:
            print(result1)
        else:
            print(result2)









# for test_case in range(1,int(input())+1):
#     def size(c):
#         result1, result2 = 0, 0
#         for i in range(0,len(c)):
#             sum1 = N[i] * M[i]
#             result1 += sum1
#         for j in range(0,len(c)):
#             sum2 = N[-j-1] * M[-j-1]
#             result2 += sum2
#         if result1 > result2:
#             print(f'#{test_case} {result1}')
#         else:
#             print(f'#{test_case} {result2}')
#
#     cnt = map(int,input().split())
#     cnt = list(cnt)
#     N = map(int,input().split())
#     M = map(int,input().split())
#     N = list(N)
#     M = list(M)
#     if cnt[0] == len(N) and cnt[1] == len(M):
#         if len(N) > len(M):
#             print(size(M))
#         else:
#             print(size(N))
#     else:
#         0