for tc in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))
    sum =0
    for i in range(2,N-2):
        if nums[i]>nums[i-1] and nums[i]>nums[i-2] and nums[i]>nums[i+1] and nums[i]>nums[i+2]:
            num = sorted(nums[i-2:i+3])
            sum += num[4]-num[3]
    print('#{} {}'.format(tc,sum))