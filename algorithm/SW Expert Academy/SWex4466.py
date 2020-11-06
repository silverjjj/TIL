for tc in range(1,int(input())+1):
    N,K = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    nums.sort()
    nums.reverse()
    sum = 0
    for i in range(K):
       sum += nums[i]
    print("#{} {}".format(tc,sum))