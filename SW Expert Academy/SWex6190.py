
n = int(input())
arr = list(map(int, input().split()))

result = 0
max_list = []
for i in range(n-1):
    num = 0
    if arr[i+1] >= arr[i]:
        num += arr[i+1]*arr[i]
        while num:
            n = num % 10    #1의자리를 얻을수있다.
            if pre < n:     #n이 이전 수보다 크면 -> 단조증가가아님
                islnc = False
                break
            num = num // 10
            pre = n



        max_list.append(sum)


    else:
        result = -1
        break
if result == -1:
    result = -1
elif result == 0:
    result = max(max_list)

print(result)
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