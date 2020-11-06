for tc in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    maxV = sum = 0
    for i in range(N-1):    # i: 0~3
        sum = (num[i+1] - num[i])
        if sum > maxV:
            maxV = sum
    print("#{} {}".format(tc+1,maxV))