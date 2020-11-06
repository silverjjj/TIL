for tc in range(1,1+int(input())):
    N = int(input())
    num = map(int,input().split())
    last = num[-1]
    sum = 0
    for i in range(N-1,-1,-1):
        if last > num[i]:
            sum += (last - num[i])
        else:
            last = num[i]
    print("#{} {}".format(tc ,sum))