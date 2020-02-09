for tc in range(1,int(input())+1):
    N = int(input())
    result = []
    for i in range(N):
        nums = list(map(float, input().split()))
        print(nums)
        result.append(nums[0]*nums[1])
    sum = 0
    for i in range(len(result)):
        sum += result[i]
    print(f"#{tc} "+'%.6f' % sum)
