#SWex6190 정곤이의 단조 증가하는수
for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))

    # n개의 값들에서 2개 선택해서 곱하는 경우
    ans = -1
    for i in range(n-1):
        for j in range(i+1,n):
            num = arr[j]*arr[i]
            if ans >= num:
                break        # 건너뛴다.

            t = num
            b = t % 10
            t //= 10
            while t:
                a = t % 10
                if a > b:
                    break
                t //=10
                b = a
            else:       # 단조증가하는수
                ans = max(ans,num)
    print(ans)



# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     maxV = -1           # 최대값을 찾기위한 변수
#
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             num = arr[i] * arr[j]
#             if i < j:           #문제에서 주어진 조건
#                 num_copy = num  #원본숫자를 조작 -> 백업
#                 pre = 10
#                 islnc = True
#                 while num:
#                     n = num % 10    #1의자리를 얻을수있다.
#                     if pre < n:     #n이 이전 수보다 크면 -> 단조증가가아님
#                         islnc = False
#                         break
#                     num = num // 10
#                     pre = n
#                 if islnc:
#                      if maxV < num_copy:
#                          maxV = num_copy
#
#     print("#{} {}".format(tc, maxV))