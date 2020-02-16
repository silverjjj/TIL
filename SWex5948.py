for tc in range(1, int(input())+1):
    nums = list(map(int, input().split()))
    sum = 0
    result = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for z in range(j+1,len(nums)):
                sum = nums[i]+nums[j]+nums[z]
                result.append(sum)

    a = set(result)
    b = []
    for i in a:
        b.append(i)
    c = sorted(b)
    print("#{} {}".format(tc, c[-5]))