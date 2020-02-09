for tc in range(1,int(input())+1):
    N = int(input())
    nums = []
    for i in range(1,1+N):
        nums.append([1]*i)
    for i in range(2,N):
        for j in range(1,i):
            nums[i][j] = nums[i-1][j-1]+nums[i-1][j]
    result = 0
    print(f"#{tc}")
    for i in range(N):
        result = " ".join(map(str,nums[i]))
        print(result)